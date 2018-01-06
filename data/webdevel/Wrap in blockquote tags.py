# Wrap the selection in blockquote tags, or just make blockquote tags
# and put the cursor inside them if the selection was empty
from scriptlib import get_sel, get_clip, set_clip, for_length_of, \
                      notify_error

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

sel = "<blockquote>" + sel + "</blockquote>"

try:
    set_clip(sel)
except Exception as e:
    notify_error(e)

time.sleep(0.01)
keyboard.send_keys("<ctrl>+v") # paste over the selection

# Put the cursor inside the <blockquote></blockquote> tags if the
# selection was empty
if no_selection:
    time.sleep(0.01)
    keyboard.send_keys(for_length_of("</blockquote>", "<left>"))

if clipb:
    time.sleep(0.1)
    set_clip(clipb) # restore previous contents (we hope)