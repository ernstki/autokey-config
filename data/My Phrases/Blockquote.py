text = ''

try:
    text = clipboard.get_clipboard()
except Exception as e:
    if e.message == "No text found in X selection":
        pass
    else:
        raise e
        
keyboard.send_key("<delete>")
keyboard.send_keys("<blockquote>%s</blockquote>" % text)