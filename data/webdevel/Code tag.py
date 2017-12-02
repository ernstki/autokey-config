from scriptlib import for_length_of
keyboard.send_keys("<")
keyboard.send_keys("code></code>")
keyboard.send_keys(for_length_of("</code>", "<left>"))

