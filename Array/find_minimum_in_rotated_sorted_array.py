"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
class Solution(object):
    def findMin(self, nums):
        """
        ~ Binary search algorithm
        - The key here is finding the inflection point: where the array flow is discontinuous.
        1. Find the mid element of the array.
        2. If mid element > first element of array this means that we need to look for the inflection point on the right of mid.
        3. If mid element < first element of array this that we need to look for the inflection point on the left of mid.
        4. We stop our search when we find the inflection point, when either of the two conditions is satisfied:
            nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
            nums[mid - 1] > nums[mid] Hence, mid is the smallest.
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        left_pointer = 0
        right_pointer = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        if nums[right_pointer] > nums[0]:
            return nums[0]

        # Binary search way
        while right_pointer >= left_pointer:
            # Find the mid element
            mid = left_pointer + (right_pointer - left_pointer) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left_pointer = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right_pointer = mid - 1
    """
    Time: O(log n)
    Space: O(1)
    """