import pyperclip

s = pyperclip.paste()
if '“' in s and '”' in s and 'Excerpt' in s:
    # remove texts before the first '“' and after the last '”'
    stripped_str = (s.split('“',1)[1]).rsplit('”',1)[0]
    # copy the string to the clipboard
    pyperclip.copy(stripped_str)
