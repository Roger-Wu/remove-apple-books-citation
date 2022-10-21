import sys
import pyperclip

def str_contains_citation(s):
    return '“' in s and '”' in s and 'Excerpt' in s

def remove_citation(s):
    # remove texts before the first '“' and after the last '”'
    stripped = (s.split('“',1)[1]).rsplit('”',1)[0]
    return stripped

# input text from stdin
multiline_str = sys.stdin.read()
if str_contains_citation(multiline_str):
    # copy the stripped string to the clipboard
    pyperclip.copy(remove_citation(multiline_str))
else:
    # copy the original string to the clipboard
    pyperclip.copy(multiline_str)
