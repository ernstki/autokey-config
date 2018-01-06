import time
from scriptlib import wrap_clip, get_clip, set_clip

# get clipboard text so we can restore it later
try:
    clip_text = get_clip()
except:
    clip_text = ''

wikitable = """\
{| class="wikitable"
 ! One
 ! Two
 |-
 | %c%|
 |-
 |}"""

lefts = wrap_clip(wikitable)
keyboard.send_keys('<ctrl>+v')

time.sleep(0.1)
keyboard.send_keys('<left>' * lefts)

if clip_text:
    time.sleep(0.1)
    set_clip(clip_text)