from os import system
from scriptlib import *

XSelectionIsEmpty = False

try:
    # See if there's anything on the clipboard:
    # url = clipboard.get_clipboard()
    url = get_clip()
except Exception as e:
    # Nope, guess there wasn't. Can't go on.
    notify_error(e.message)
    
try:
    # See if there's anything in the X selection:
    linktext = get_sel()
except EmptyXSelection as e:
    XSelectionIsEmpty = True
except Exception as e:
    # Something else went wrong:
    notify_error(e.message)

if XSelectionIsEmpty:
    # Paste the contents of the clipboard in the href attribute, then put the
    # cursor back between the opening and closing tags:
    keyboard.send_keys("<a title=\"\" href=\"%s" % url)
    keyboard.send_keys('"></a>')
    keyboard.send_key('<left>', 4)     
else:
    # Create the <a> tag around the X selection:
    keyboard.send_keys("<a title=\"\" href=\"%s" % url)
    keyboard.send_keys("\">%s" % linktext )
    keyboard.send_keys('</a>')