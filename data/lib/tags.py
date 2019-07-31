# functions for wrapping things in arbitrary text (tags)
from scriptlib import get_clip, set_clip, notify_error

def wrap_tag(tag):
    clipboard_empty = False
    try:
        clip = get_clip()
    except:
        clip = ""
        clipboard_empty = True

    clip = "<{0}>{1}</{0}>".format(tag, clip)

    try:
        set_clip(clip)
    except Exception as e:
        notify_error(e)