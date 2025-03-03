# TwoSum solution
# given a list of ints and a target number, find the indices of two elements in list that equal target
# if none can be found, return an empty list
# the two indices cannot be the same, i.e. i != j
def two_sum(nums: list[int], target: int) -> list[int]:
    prevSeenMap = {} # key->value will be val->index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevSeenMap:
            return [prevSeenMap[diff], i]
        else:
            prevSeenMap[n] = i
    return []

# tests
print(two_sum([3,4,5,6], 7)) #[0,1]
print(two_sum([4,5,6], 10)) #[0,2]
print(two_sum([1,2,3,4], 8)) #[]