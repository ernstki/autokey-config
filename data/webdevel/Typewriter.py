# Wrap the selected text in "teletype" tags (<tt></tt>)
from scriptlib import get_sel, get_clip, set_clip, for_length_of

no_selection = False
try:
    sel = get_sel()
except:
    sel = ""
    no_selection = True
try:
    clip_text = get_clip() # because we're about to clobber it
except:
    clip_text = ""

sel = "<tt>" + sel + "</tt>"

try:
    set_clip(sel)
except Exception as e:
    notify_error(e)

time.sleep(0.01)
keyboard.send_keys("<ctrl>+<shift>+v") # paste over the selection

# Put the cursor inside the <tt></tt> tags if the selection was empty
if no_selection:
    time.sleep(0.01)
    keyboard.send_keys(for_length_of("</tt>", "<left>"))

if clip_text: 
    time.sleep(0.1)
    set_clip(clip_text) # restore previous contents