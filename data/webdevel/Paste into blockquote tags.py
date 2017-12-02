from scriptlib import *

clipboard_empty = False
try:
    clip = get_clip()
except:
    clip = ""
    clipboard_empty = True

clip = "<blockquote>" + clip + "</blockquote>"
set_clip(clip)
time.sleep(0.01)
keyboard.send_keys("<ctrl>+v") # paste over the selection