def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i


testedArray = [1, 2, 2, 3, 4, 5, 8, 8, 9]
print(removeDuplicates(testedArray))
