# Wrap the clipboard text in a print_r for PHP debugging
import time
from scriptlib import get_clip, set_clip, wrap_clip

DELAY = 0.08
START = 'echo "<pre>"; print_r('
END = '); echo "</pre>\\n";'

# get clipboard contents so we can restore later
try:
    clip_text = get_clip()
except:
    clip_text = ''
  
lefts = wrap_clip(START + '%c' + END, clip_text=clip_text)
keyboard.send_keys('<shift>+<ctrl>+v')

time.sleep(DELAY)
keyboard.send_keys('<left>' * lefts)

if clip_text:
    time.sleep(DELAY)
    set_clip(clip_text)