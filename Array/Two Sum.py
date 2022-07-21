'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''
def twoSums(nums, integer):
    """
    1. create a dict. key will be the integer difference between target and nums[i], value is index of nums[i].
    2. loop thro' the array, check if current element is in the dict, if it is, return current index and value from the dict.
        - else, create a dict entry with difference as key and index as the value.
    """
    diff_dict = {}
    for i in range(0, len(nums)):
        if nums[i] in diff_dict:
            return (i, diff_dict[i])
        else:
            diff_dict[integer - nums[i]] = i

"""
Complexity.
- Time is O(n) - we are looping through all elements
- Space is O(n) - for the dict
"""
def twoSums(nums, integer):
    """
    solution with two pointers
    """
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum < integer:
            left += 1
        elif sum > integer:
            right -= 1
        else:
            return (left, right)
        while left < right and nums[left] == nums[left-1]:
            left += 1
        while left < right and nums[right] == nums[right+1]:
            right -= 1
    return None
"""
Complexity.
- Time is O(nlog(n)) - we are sorting the array
- Space is O(1)
"""