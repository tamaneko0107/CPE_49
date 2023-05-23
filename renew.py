from sys import stdin

s = stdin.readlines()
s = ''.join(s)
s.rstrip()
for i in range(s.count('"')//2):
    s = s.replace('"', '``', 1)
    s = s.replace('"', "\'\'", 1)
print(s, end='')
