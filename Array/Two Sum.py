'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''
def twoSums(nums, integer):
    """
    1. create a dict.
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