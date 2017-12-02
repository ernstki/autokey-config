from os import system
from subprocess import (Popen, PIPE)

ERR_NOXSEL = "No text found in X selection"
ERR_NOCLIP = "No text found on clipboard"

class ScriptLibException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class EmptyXSelection(ScriptLibException):
    def __init__(self, value):
        self.value = ERR_NOXSEL
    def __str__(self):
        return repr(self.value)
        
class EmptyClipboard(ScriptLibException):
    def __init__(self, value):
        self.value = ERR_NOCLIP
    def __str__(self):
        return repr(self.value)

def error_notify(msg):
    system( 'notify-send -u critical -i dialog-warning "AutoKey script" "%s"' % msg )
    raise
    
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
        raise RuntimeError('Problem running xclip in get_clip()')
    finally:
        if len(clip) == 0:
            raise EmptyClipboard('X clipboard is empty')
    return clip.decode('utf-8')

def set_sel(sel):
    try:
        Popen(['xclip', '-selection', 'primary', '-i'],
              stdin=PIPE).communicate(sel)
    except Exception as e:
        raise RuntimeError('Problem setting X selection')

def set_clip(clip):
    try:
        Popen(['xclip', '-selection', 'clipboard', '-i'],
              stdin=PIPE).communicate(clip)
    except Exception as e:
        raise RuntimeError('Problem setting clipboard')


# scriptlib.py
