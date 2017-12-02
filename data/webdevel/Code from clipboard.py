from scriptlib import error_notify, for_length_of
 
code = ''
lang = 'bash'  # default syntax highlighting language
xsel = True    # there was an X selection (PRIMARY)

try:
    code = clipboard.get_selection()
except Exception as e:
    if e == 'No text found in X selection':
        pass

# if X selection was empty, try clipboard
if not code:
    xsel = False
    try:
        code = clipboard.get_clipboard()
    except Exception as e:
        if e == 'No text found on clipboard':
            pass

if xsel:
    # wipe out whatever was selected
    keyboard.send_keys("<delete>")
    
# ask user what language to use for highlighting (prism.js style)
(ret, lang) = dialog.input_dialog(
    title='Code block from clipboard',
    message='Syntax highlighting class for clipboard contents?',
    default=lang)
    
attr = (' class="language-%s"' % lang) if lang and ret==0 else ''
        
# give the previous window enough time to get focused
time.sleep(0.1)

# <code> is a "special key" to AutoKey, so this is necessary :-(
keyboard.send_key("<")
keyboard.send_keys("code%s>" % attr)

if code:
    keyboard.send_keys("<enter>")
    keyboard.send_keys(code)
    keyboard.send_keys("<enter>")
    keyboard.send_keys("</code>")
else:
    keyboard.send_keys("</code>")
    # put the cursor between the tags
    keyboard.send_keys(for_length_of("</code>", "<left>"))