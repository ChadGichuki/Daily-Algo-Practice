class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Source: https://leetcode.com/problems/two-sum/
    """
    def twoSum(self, nums: list, target: int):
        hashTable = {}
        for index, value in enumerate(nums):
            # enumerate() returns a index/value pair
            if target - value in hashTable:
                # If the 2nd value needed to sum up the current value to the target is in the hashtable already, return
                return([index, hashTable[target-value]])
            hashTable[value] = index
            # Else store the current value as a key and it's index as the value in the hashtable


test = Solution()
print(test.twoSum([1,5,7,8,9], 15))
# 7 + 8 = 15
# expects [2, 3]