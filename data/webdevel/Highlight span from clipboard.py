# Wrap clipboard text in a highlighter style span from this JSFiddle
# http://jsfiddle.net/qnGKj/2987/
from scriptlib import get_clip, set_clip, notify_error

clipboard_empty = False
try:
    clip = get_clip()
except:
    clip = ""
    clipboard_empty = True

clip = '<span style="border-radius:1em/1em 0.1em;display:inline-block;'\
       'padding:0 0.05em;background:rgba(255,215,0,0.5);">' + clip + \
       '</span>'

try:
    set_clip(clip)
except Exception as e:
    notify_error(e)

time.sleep(0.01)
keyboard.send_keys("<shift>+<ctrl>+v")