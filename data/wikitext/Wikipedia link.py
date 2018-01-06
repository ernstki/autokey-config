import time
from scriptlib import wrap_clip, get_clip, set_clip

# save the clipboard so we can restore it
try:
    oldclip = get_clip()
except:
    # catches errors or an empty clipboard
    oldclip = ''

# wrap_clip returns the # of times to press <left> to get cursor in
# the position specified in the format string ('%|')
lefts = wrap_clip('[[wp:%c%||%c]]')
keyboard.send_keys("<ctrl>+v")

# give it a tick...
time.sleep(0.1)
keyboard.send_keys('<left>' * lefts)

if oldclip:
    time.sleep(0.1)
    set_clip(oldclip) # restore previous clipboard contents