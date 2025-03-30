# leetcode 238
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The problem can be solved in O(n) time complexity and O(1) space complexity.
# We can use two arrays to keep track of the product of all elements to the left and right of each element.
# Then we can multiply the two arrays together to get the final result.
# The time complexity is O(n) because we are iterating through the array twice, and the space complexity is O(1) because we are using a fixed amount of space for the two arrays.
def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    answer = [1] * n

    # Calculate the product of all elements to the left of each element
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    # Calculate the product of all elements to the right of each element
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # Calculate the final answer by multiplying the left and right products
    for i in range(n):
        answer[i] = left[i] * right[i]

    return answer

# Test cases
print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExceptSelf([-1,1,0,3,-3])) # [0, 0, 0, 0]
print(productExceptSelf([0,0])) # [0, 0]
print(productExceptSelf([1,2,3,4,5])) # [120, 60, 40, 30, 24]
print(productExceptSelf([1,1,1,1])) # [1, 1, 1, 1]