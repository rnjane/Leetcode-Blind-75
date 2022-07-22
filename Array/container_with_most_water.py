
"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""
class Solution:
    """
    - We use two pointers to find the max area, one starting from the start and the other at the end of the array.
    - The area between the two pointers is the product of the minimum of the two heights(where the pointers are at) 
        and the distance between the pointers.
    - we move the pointers towards each other until the distance between the pointers is 0.
        - all along, we re-compute the area between the two pointers and update max_area if the area is greater than max_area.
    """
    # NOTE: MORE EFFICIENT SOLUTION
    def maxArea(self, height) -> int:
        max_area = 0 
        left_pointer = 0 
        right_pointer = len(height)-1
        while left_pointer < right_pointer:
            minHeight = min(height[left_pointer], height[right_pointer])
            max_area = max(max_area, minHeight * (right_pointer-left_pointer))
            while left_pointer < right_pointer and height[left_pointer] <= minHeight:
                left_pointer += 1 
            while left_pointer < right_pointer and height[right_pointer] <= minHeight:
                right_pointer -= 1
        return max_area

    # def maxArea(self, height) -> int:
    #     left_pointer = 0
    #     right_pointer = len(height) - 1
    #     max_area = 0
    #     while left_pointer < right_pointer:
    #         max_area = max(max_area, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
    #         if height[left_pointer] < height[right_pointer]:
    #             left_pointer += 1
    #         else:
    #             right_pointer -= 1
    #     return max_area

"""
Time: O(n)
Space: O(1)
"""