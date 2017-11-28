(ret, syn) = dialog.input_dialog(
    title='Code block from clipboard',
    message='Syntax highlighting class for clipboard contents?',
    default='bash')

code = ''
lang = (' class="language-%s"' % syn) if syn and ret==0 else '' 


try:
    code = clipboard.get_clipboard()
except Exception as e:
    if e.message == "No text found in X selection":
        pass
    else:
        raise e
        
#keyboard.send_key("<delete>")
# <code> is a "special key" to AutoKey, so this is necessary :-(
keyboard.send_key("<")
keyboard.send_keys("code%s><enter>%s<enter></code>" % (lang,code))