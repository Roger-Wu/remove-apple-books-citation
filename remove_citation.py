import sys

def str_contains_citation(s):
    return '“' in s and '”' in s and 'Excerpt' in s

def remove_citation(s):
    if str_contains_citation(s):
        # extract texts between the first '“' and the last '”'
        stripped = (s.split('“',1)[1]).rsplit('”',1)[0]
        return stripped
    return s

# input text from stdin
multiline_str = sys.stdin.read()
print(remove_citation(multiline_str))
