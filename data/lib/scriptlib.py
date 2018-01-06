import re
import time
from os import system
from subprocess import (Popen, PIPE)

ERR_NOXSEL = "No text found in X selection"
ERR_NOCLIP = "No text found on clipboard"

class ScriptLibException(Exception):
    def __init__(self, message):
        self.message = message
    def __repr__(self):
        return self.message

class EmptyXSelection(ScriptLibException):
    def __init__(self, message):
        self.message = ERR_NOXSEL
    def __repr__(self):
        return self.message

class EmptyClipboard(ScriptLibException):
    def __init__(self, message):
        self.message = ERR_NOCLIP
    def __repr__(self):
        return self.message


def notify_error(msg, level='normal', reraise=True, bail=False,
                 icon='warning'):
    """
    Use 'notify-send' to send a desktop notification of an error.
    
    Optionally, quit the script if 'bail' parameter is True.
    
    At the present time, I'm not sure if 'reraise' does anything, but
    I think it causes the script to terminate if notify_error() was
    called inside an exception handler. Maybe?
    """
    system("notify-send -u %s -i dialog-%s 'AutoKey script' '%s'"
           % (level, icon, msg))
    if bail:
        exit(1)
    if reraise:
        raise
        
        
def notify_warn(msg, level='normal', reraise=True):
    """
    Same as above, except don't terminate the script
    """
    notify_error(msg, level, reraise=False, icon='information')
    

def get_sel():
    try:
        sel = Popen(['xclip', '-selection', 'primary', '-o'],
                    stdout=PIPE).communicate()[0]
    except Exception as e:
        raise RuntimeError('Problem running xclip in get_sel()')
    finally:
        if len(sel) == 0:
            raise EmptyXSelection('X selection is empty')
    # source: https://stackoverflow.com/a/606199
    return sel.decode('utf-8')
        

def get_clip():
    try:
        clip = Popen(['xclip', '-selection', 'clipboard', '-o'],
                     stdout=PIPE).communicate()[0]
    except Exception as e:
        raise RuntimeError("Problem running xclip in get_clip (%s)", e)
    finally:
        if len(clip) == 0:
            raise EmptyClipboard('X clipboard is empty')
    return clip.decode('utf-8')


def set_sel(sel):
    try:
        Popen(['xclip', '-selection', 'primary', '-i'],
              stdin=PIPE).communicate(sel.encode())
    except Exception as e:
        raise RuntimeError("Problem setting X selection (%s)" % e)


def set_clip(clip):
    try:
        Popen(['xclip', '-selection', 'clipboard', '-i'],
              stdin=PIPE).communicate(clip.encode())
    except Exception as e:
        raise RuntimeError("Problem setting clipboard (%s)" % e)


def for_length_of(s1, s2):
    """
    Return a string consisting of s2 repeated for each character that
    s1 is long
    """
    return ''.join([s2 for _ in range(0, len(s1))])         

        
def wrap_clip(format_string, clip_text=None):
    """
    Wrap the clipboard contents in arbitrary text.
      
    The format_string parameter should look something like
    
        <before>%c%|</after>

    where '%c' is the clipboard contents and '%|' is the final cursor
    position.

    If 'clip_text' is provided, it is used to replace the '%c' token in
    lieu of the clipboard.
    
    FIXME: dunno how to keyboard.send_keys() within an included
    library in AutoKey ('import autokey.scripting' doesn't work), so
    this function isn't actually positioning the cursor for you, or
    re-setting the clipboard when it's done. For now, you have to do
    that in the calling AutoKey script.
    
    If '%|' is found in the format_string, the cursor is put exactly
    there, regardless of whether some text was on the clipboard.
    
    If '%|' is NOT found in format_string, the cursor is put at the is
    placed right before the "after" text (e.g., right before the closing
    HTML tag) if the clipboard was empty, otherwise it's placed at the
    very end of the inserted text.
    
    The LAST occurrence of '%c' in format_string is used to determine
    what the "after" text is.
    
    If '%c' isn't found in format_string, an exception is raised.
    
    Returns:
        the number of times to press <left> to get the cursor in
        the position specified with the "cursor here" token in
        format_string.
    """
    if not format_string:
        raise ScriptLibException('Non-empty string argument required')

    if clip_text is None:
        try:
            clip_text = get_clip()
        except:
            # this catches errors and an empty clipboard
            clip_text = ''

    # split the input string at the places where user wants to insert
    # the contents of the clipboard
    clip_parts = re.split('%c', format_string)
    
    if len(clip_parts) == 1:
        # there was no '%c to split on
        raise ScriptLibException("Missing '%c' (clipboard insert position) "
                                 "in 'format_string'")

    # because of Python's wacky join() syntax, this means: stick 'parts'
    # together with 'clip' in between each one.
    replacement = clip_text.join(clip_parts)
    
    # divide the replacement string at the "cursor here" token ('%|')
    cursor_parts = re.split('%\|', replacement)
    
    # if '%|' *is* found in the format_string...
    if len(cursor_parts) > 1:
        # the *last* "cursor here" token is honored; others are ignored
        after = cursor_parts[-1]
        # stitch back together without the '%|'
        replacement = ''.join(cursor_parts)
    else:
        # if there was nothing on the clipboard, put the cursor right
        # before the last chunk of literal text from the format string,
        # otherwise, put the cursor at the end of the inserted text
        after = clip_parts[-1] if not clip_text else ''
        
    try:
        set_clip(replacement)
        time.sleep(0.1)  # FIXME: pause for the subprocess to finish
    except Exception as e:
        notify_error(e)  # this terminates the script
        
    # return the number of times to press the left arrow key
    return len(after)
        
# scriptlib.py