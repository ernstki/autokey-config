# Note that this does the same thing as "Blockquote tags" does when
# there's no selection, except that that one has an abbreviation and 
# and this has a hotkey.
from scriptlib import get_clip, set_clip, for_length_of, error_notify

clipboard_empty = False

try:
    oldclip = get_clip() # because we're about to clobber it
    clip = "[[wp:" + oldclip + "|" + oldclip + "]]"
except:
    # this catches errors and an empty clipboard
    cliboard_empty = True
    clip = "[[wp:]]" 

try:
    set_clip(clip)
except Exception as e:
    error_notify(e)  # this terminates the script

time.sleep(0.1)
keyboard.send_keys("<ctrl>+v")

# Put the cursor inside the wikilink if the clipboard was empty
if clipboard_empty:
    time.sleep(0.1)
    keyboard.send_keys("<left><left>")
else:
    time.sleep(0.1)
    set_clip(oldclip) # restore previous clipboard contents