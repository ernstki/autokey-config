# Enter script code

key1 = 10
key2 = 11
key3 = 12
key4 = 13

grabthesekeys = [key1, key2, key3, key4]

from Xlib.display import Display
from Xlib import X

keyboard.send_keys("<shift>+<tab>" +
    "<shift>+<tab>" +
    " ")
    
# current display
disp = Display()
root = disp.screen().root

# we tell the X server we want to catch keyPress event
root.change_attributes(event_mask = X.KeyPressMask)

for keycode in grabthesekeys:
    root.grab_key(keycode, X.AnyModifier, True, X.GrabModeAsync, X.GrabModeAsync)

# display*		 Specifies the connection to the X server.
# keycode	 	 Specifies the KeyCode or AnyKey.
# modifiers	 	 Specifies the set of keymasks or AnyModifier. The mask
#                is the bitwise inclusive OR of the valid keymask bits.
# grab_window*	 Specifies the grab window.
# owner_events	 Specifies a Boolean value that indicates whether the
#                keyboard events are to be reported as usual.
# pointer_mode	 Specifies further processing of pointer events. You
#                can pass GrabModeSync or GrabModeAsync.
# keyboard_mode	 Specifies further processing of keyboard events. You
#                can pass GrabModeSync or GrabModeAsync.
#
# (*not in python-xlib)

# Get one key event, thass all:
event = root.display.next_event()
for keycode in grabthesekeys:
    root.ungrab_key(keycode, X.AnyModifier, None)



    

    
