''' 217. Contains Duplicate - Easy

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
 
Example 1:
    Input: [1,2,3,1]
    Output: true

Example 2:
    Input: [1,2,3,4]
    Output: false

Example 3:
    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
'''
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sort nums
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                return True
        return False

n1 = [1,2,3,1]
n2 = [1,2,3,4]
n3 = [1,1,1,3,3,4,3,2,4,2]

S1 = Solution()

print(S1.containsDuplicate(n1)) # True
print(S1.containsDuplicate(n2)) # False
print(S1.containsDuplicate(n3)) # True