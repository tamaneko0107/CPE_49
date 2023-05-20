# s = []
# for i in range(7):
#     s.append(input())

# print(set(map(lambda x: ''.join(set(x[1:4])), s[0:3])))
# print(set(str(s[1][2])))

# import sys

# for i in sys.stdin:
#     if not i[:-1]:
#         break
#     print(i[:-1])

# print("e")

# s = ["456", "123"]


# print('\n'.join(s))

s = [2, 3, 1, 4, 9, 12, 8]
#   [2, 0, 1, 1, 0, 0 , 2]


def so(x):

    return (x % 3, x % 2 == 1, -x if x % 2 == 1 else x)


print(sorted(s, key=lambda x: x % 3))
sorted_s = sorted(s, key=so)
print(sorted_s)
