# Two Sum Leetcode 1(Hashmap)
# use a hashmap to store the indices of the elements
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return []
    
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(Solution().twoSum([3,3], 6))
