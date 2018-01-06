import re
import time
from scriptlib import wrap_clip, get_clip, get_sel, set_clip, \
                      notify_warn

# save the clipboard so we can restore it
try:
    oldclip = get_clip()
except:
    # catches errors or an empty clipboard
    oldclip = ''

if not re.match('[a-zA-Z]+://', oldclip):
    notify_warn('No URL found on clipboard') 

try:
    selection = get_sel()
except:
    selection = ''

# wrap_clip returns the # of times to press <left> to get cursor in
# the position specified in the format string ('%|')
lefts = wrap_clip('[%%c %s]' % selection)
keyboard.send_keys("<ctrl>+v")

# give it a tick to finish pasting that...
time.sleep(0.1)
keyboard.send_keys('<left>' * lefts)

if oldclip:
    time.sleep(0.1)
    set_clip(oldclip) # restore previous clipboard contents