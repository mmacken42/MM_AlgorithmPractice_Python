# TwoSum solution
# given a list of ints and a target number, find the indices of two elements in list that equal target
# if none can be found, return an empty list
# the two indices cannot be the same, i.e. i != j
def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        first_num = nums[i]
        for j in range(i + 1, len(nums)):
            second_num = nums[j]
            if first_num + second_num == target:
                return [i, j]
    return []

# tests
print(two_sum([3,4,5,6], 7)) #[0,1]
print(two_sum([4,5,6], 10)) #[0,2]
print(two_sum([1,2,3,4], 8)) #[]

#this was a brute force solution, not ideal
#nested for loops makes time complexity O(n^2)
#space complexity would be O(1)
