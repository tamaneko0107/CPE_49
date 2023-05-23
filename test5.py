def find_sum_combinations(nums, target):
    result = []

    def backtrack(path, start, target):
        if target == 0:
            result.append(path[:])
        elif target < 0:
            return
        else:
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i, target - nums[i])
                path.pop()

    backtrack([], 0, target)
    return result


# 測試程式碼
nums = [2, 4, 6, 3]
target = 8

combinations = find_sum_combinations(nums, target)
for combination in combinations:
    print(combination)
