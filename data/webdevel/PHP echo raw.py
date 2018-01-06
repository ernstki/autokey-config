# Wrap the selection text in a PHP 'print_r' statement for debugging If
# selection is empty, just put the cursor inside the 'print_r()'
import time
from scriptlib import get_sel, get_clip, set_clip

# get existing clipboard text, so we can restore it
try:
    clip_text = get_clip()
except:
    clip_text = ''

try:
    sel = get_sel()
except:
    sel = ''
    
set_clip(sel)

engine.run_script('PHP echo raw (from clipboard)')

if clip_text:
    time.sleep(0.1)
    set_clip(clip_text)
