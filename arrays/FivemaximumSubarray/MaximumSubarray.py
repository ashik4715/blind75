# Maximum subarray (53.Leetcode):
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

def maxSubArray(nums: list[int]) -> int:
    """
    Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.
    :param nums: List[int]: input list of integers
    :return: int: maximum subarray sum
    """
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

# Test cases
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6  
print(maxSubArray([1]))  # Output: 1
print(maxSubArray([5, 4, -1, 7, 8]))  # Output: 23