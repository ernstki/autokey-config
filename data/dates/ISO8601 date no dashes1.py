from datetime import datetime as dt
keyboard.send_keys(dt.now().strftime('%Y%m%d'))

# alternatively,
#import time
#keyboard.send_keys(time.strftime "%Y%m%d", time.gmtime()))