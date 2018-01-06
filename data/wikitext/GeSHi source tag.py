# Wrap the selection (or clipboard contents, if the selection is empty)
# with <source> tags and moves the cursor back to the 'lang=""' part
import time
from scriptlib import wrap_clip, get_clip, get_sel, set_clip, \
                      notify_warn

DELAY = 0.08
OPEN_TAG = '<source lang="%|">'
CLOSE_TAG = '</source>'

# save the clipboard so we can restore it
try:
    clip_text = get_clip()
except:
    # catches errors or an empty clipboard
    clip_text = ''
    
try:
    selection = get_sel()
except:
    selection = ''
    
# if there's an active selection, this takes precedence over the
# clipboard contents
replacement_text = selection if selection else clip_text

# wrap_clip returns the # of times to press <left> to get cursor in
# the position specified in the format string ('%|')
lefts = wrap_clip(OPEN_TAG + '\n%c\n' + CLOSE_TAG, clip_text=replacement_text)
keyboard.send_keys("<ctrl>+v")

# give it a tick to finish pasting that...
time.sleep(DELAY)
keyboard.send_keys('<left>' * lefts)

if clip_text:
    time.sleep(DELAY)
    set_clip(clip_text) # restore previous clipboard contents