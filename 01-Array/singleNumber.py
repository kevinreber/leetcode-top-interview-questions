''' 136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:
    Input: nums = [2,2,1]
    Output: 1

Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1
 
Constraints:
    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

'''
class Solution:
    def singleNumber(self, nums):
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for num in count:
            if count[num] == 1:
                return num

S = Solution()

n1 = [2,2,1]
n2 = [4,1,2,1,2]
n3 = [1]

print(S.singleNumber(n1)) # 1
print(S.singleNumber(n2)) # 4
print(S.singleNumber(n3)) # 1