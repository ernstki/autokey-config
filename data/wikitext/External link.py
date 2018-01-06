# Wraps the selection in the 

import re
import time
from scriptlib import wrap_clip, get_clip, get_sel, set_clip, \
                      notify_warn

# save the clipboard so we can restore it
try:
    clip_text = get_clip()
except:
    # catches errors or an empty clipboard
    clip_text = ''
    
if re.match('[a-zA-Z]+://', clip_text):
    url = clip_text
else:
    notify_warn('No URL found on clipboard')
    url = ''

try:
    selection = get_sel()
except:
    selection = ''

# wrap_clip returns the # of times to press <left> to get cursor in
# the position specified in the format string ('%|')
lefts = wrap_clip('[%c ' + selection + ']', clip_text=url)
keyboard.send_keys("<ctrl>+v")

# give it a tick to finish pasting that...
time.sleep(0.1)
keyboard.send_keys('<left>' * lefts)

if clip_text:
    time.sleep(0.1)
    set_clip(clip_text) # restore previous clipboard contents