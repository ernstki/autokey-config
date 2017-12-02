import time

INTERKEY_DELAY = 0.08

open_tag       = '<source lang="">'
close_tag      = '</source>'

time.sleep(INTERKEY_DELAY)
keyboard.send_keys(open_tag)
time.sleep(INTERKEY_DELAY)
keyboard.send_keys('<enter>' + close_tag)
time.sleep(INTERKEY_DELAY*2)

#keyboard.send_keys(''.join(['<left>' for _ in range(0, len(close_tag) + 3)]))
for _ in range(0, len(close_tag) + 3):
    keyboard.send_keys('<left>')
    time.sleep(INTERKEY_DELAY/3.0)
