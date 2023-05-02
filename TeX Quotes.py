s = ""
while True:
    try:
        s += input()
        s += "\n"
    except EOFError:
        break

s.rstrip()
for _ in range(int(s.count('"')/2)):
    s = s.replace('"', "``", 1)
    s = s.replace('"', "\'\'", 1)
print(s, end="")
