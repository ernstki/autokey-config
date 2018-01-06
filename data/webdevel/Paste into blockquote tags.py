# Same basic thing as "Wrap in blockquote tags" except it ignores
# any selected text (and is maybe a bit simpler)
from scriptlib import get_clip, set_clip, notify_error

clipboard_empty = False
try:
    clip = get_clip()
except:
    clip = ""
    clipboard_empty = True

clip = "<blockquote>" + clip + "</blockquote>"

try:
    set_clip(clip)
except Exception as e:
    notify_error(e)

time.sleep(0.01)
keyboard.send_keys("<ctrl>+v") # paste over the selection