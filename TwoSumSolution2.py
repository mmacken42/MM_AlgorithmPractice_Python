# TwoSum solution
# given a list of ints and a target number, find the indices of two elements in list that equal target
# if none can be found, return an empty list
# the two indices cannot be the same, i.e. i != j
def two_sum(nums: list[int], target: int) -> list[int]:
    # want to solve nums[i] + nums[j] = target and return i and j if they exist
    prevSeenMap = {} # val -> index
    for i, n in enumerate(nums): #where i is the index and n is the value at that index
        difference = target - n #does this "difference" exist elsewhere in nums?
        if difference in prevSeenMap:
            return [prevSeenMap[difference], i]
        prevSeenMap[n] = i
    return []

# tests
print(two_sum([3,4,5,6], 7)) #[0,1]
print(two_sum([4,5,6], 10)) #[0,2]
print(two_sum([1,2,3,4], 8)) #[]

#this is pretty ideal. time complexity reduced but we do use inc. space complexity
#nested for loops makes time complexity O(n)
#space complexity would be O(n)