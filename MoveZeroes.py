def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    ptr = 0
    numZeroesToAppend = 0
    while ptr < len(nums):
        if nums[ptr] == 0:
            numZeroesToAppend += 1
            nums.remove(nums[ptr])
            #no need to increment ptr because we just removed an element, so ptr is automatically pointed at next element
        else:
            ptr += 1

    while numZeroesToAppend > 0:
        nums.append(0)
        numZeroesToAppend -= 1

    #no return, we just modify nums in-place