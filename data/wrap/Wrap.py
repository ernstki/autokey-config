# I can't seem to make this work without hard-coding 'wrap' and
# 'wrap_close' in the other script; even 'global' doesn't work
#
# source: https://github.com/autokey/autokey/wiki/Scripting#advanced-scripts

wrap = "(" 
wrap_close = ")"
engine.run_script("wrap_selection")