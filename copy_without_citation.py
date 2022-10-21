import sys
import pyperclip

# input text from stdin
multiline_str = sys.stdin.read()
# remove texts before the first '“' and after the last '”'
stripped_str = (multiline_str.split('“',1)[1]).rsplit('”',1)[0]
# copy the string to the clipboard
pyperclip.copy(stripped_str)
