"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, 
nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    """
    - we use binary search to find the target
    - we initialize left and right pointers to the start and end of the array
    - we keep looping until left pointer is less than or equal to right pointer
    - we find the mid point of the array
    - if the target is equal to the mid point then we return the mid point.

    A rotated array has one half that is sorted. To find out which:
        - if the midpoint value is less than or equal to the first element, then the left part is sorted.
        - else, the right part is sorted.
    - After identifying the sorted part of the array, we use normal binary search to find the target value.
    We return -1.

    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                # if target is greater than midpoint value, or less than the leftmost value of the array, then
                # we know that the target is not in the left array. We move left pointer to the midpoint + 1.
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1