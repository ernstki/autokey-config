# If you want the window filter to work, remember that it's a real regexp, so
# you'll need something like ".*KeePassX" to actually match the right window

# Selects the bottom-most bookmark in the list
import time
keyboard.send_keys('<alt>+f')
time.sleep(0.2)
keyboard.send_key('b')
time.sleep(0.2)
#keyboard.send_key('<up>')
keyboard.send_key('<up>')
keyboard.send_key('<up>')
time.sleep(0.2)
keyboard.send_key('<enter>')
time.sleep(0.2)
# The unlock dialog doesn't get focus without this:
system.exec_command('wmctrl -a .kdb')