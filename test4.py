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


# def so(x):

#     return (x % 3, x % 2 == 1, -x if x % 2 == 1 else x)


# print(sorted(s, key=lambda x: x % 3))
# sorted_s = sorted(s, key=so)
# print(sorted_s)
# s = "sa"
# print(dir(s))

def find_sum_combinations(nums, target):
    result = []
    
    def backtrack(path, start, target):
        if target == 0:
            result.append(path[:])
        elif target < 0:
            return
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, i+1, target - nums[i])  # 注意這裡的 i+1
                path.pop()
    
    nums.sort()  # 需要先將數組排序，以確保相同的元素相鄰
    backtrack([], 0, target)
    return result


# 測試程式碼
nums = [2, 4, 4, 6, 3,2,2,2]
target = 8

combinations = find_sum_combinations(nums, target)
for combination in combinations:
    print(combination)
