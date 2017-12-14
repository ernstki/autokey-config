# Note that this is just a copy-paste of "Wrap in blockquote tags"
from scriptlib import get_sel, get_clip, set_clip, for_length_of

no_selection = False
try:
    sel = get_sel()
except:
    sel = ""
    no_selection = True
try:
    clipb = get_clip() # because we're about to clobber it
except:
    clipb=""

sel = "<tt>" + sel + "</tt>"

try:
    set_clip(sel)
except Exception as e:
    error_notify(e)

time.sleep(0.01)
keyboard.send_keys("<ctrl>+v") # paste over the selection

# Put the cursor inside the <blockquote></blockquote> tags if the
# selection was empty
if no_selection:
    time.sleep(0.01)
    keyboard.send_keys(for_length_of("</tt>", "<left>"))

# The set_clip() command is too slow for this to be reliable, since
# we're calling out to 'xclip' with Popen():
#set_clip(clipb) # restore previous contents (we hope)