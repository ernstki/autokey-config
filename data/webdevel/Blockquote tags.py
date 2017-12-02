# Note that this does the same thing as "Wrap in blockquote tags"
# does when there's no selection, except that's bound to a hotkey
# and this has an abbreviation.
keyboard.send_keys('<blockquote></blockquote>')
keyboard.send_keys(''.join(['<left>' for _ in range(0, len('</blockquote>'))]))