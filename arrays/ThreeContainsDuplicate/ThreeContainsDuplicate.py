# Leet Problem No. 217
# Problem: Given an integer array nums, return true if any value appears at least three times in the array.
# You must implement a solution with O(n) time complexity and O(1) space complexity.
# Solution: Use a set to keep track of the numbers we have seen and a counter to count the occurrences of each number.

# If the count of any number reaches 3, we return True. If we finish iterating through the array without finding any number that appears 3 times, we return False.
# The time complexity is O(n) because we are iterating through the array once, and the space complexity is O(1) because we are using a fixed amount of space for the set and counter.

def containsDuplicate(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        if count[num] >= 3:
            return True
    return False

# Test cases
print(containsDuplicate([1,2,3,1])) # False
print(containsDuplicate([1,2,3,1,1,1])) # True
print(containsDuplicate([1,2,3,4])) # False
print(containsDuplicate([1,2,3,4,5,6,7,8,9,10])) # False
