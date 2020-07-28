import re
def solution(s):
    if len(s) % 2 != 0:
        s = s + '_'
    a = re.findall('..?', s)
    return a