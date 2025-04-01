# Leetcode 152. Maximum Product Subarray:
# Given an integer array nums, find a contiguous non-empty subarray within the array (containing at least one number) which has the largest product, and return that product.
# The test cases are included in the code.
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6

def maximumProductSubArray(nums: list[int]) -> int:
    """
    Find the contiguous non-empty subarray within the array (containing at least one number) which has the largest product, and return that product.
    :param nums: List[int]: input list of integers
    :return: int: maximum product of subarray
    """
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        result = max(result, max_product)

    return result

# Test cases
print(maximumProductSubArray([2, 3, -2, 4]))  # Output: 6
print(maximumProductSubArray([-2,0,-1])) # Output: 0
print(maximumProductSubArray([3,-1,4])) # Output: 4
print(maximumProductSubArray([2,-5,-2,-4,3])) # Output: 24
print(maximumProductSubArray([3,-1,4,-1])) # Output: 12
print(maximumProductSubArray([2,-5,-2,-4,-1,3])) # Output: 240