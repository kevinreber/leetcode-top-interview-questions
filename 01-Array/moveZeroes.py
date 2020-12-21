''' 283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example 1:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    1. You must do this in-place without making a copy of the array.
    2. Minimize the total number of operations.

'''
class Solution:
    def moveZeroes(self, nums):
        '''Using 2 pointers'''
        i = 0
        j = 1
        n = len(nums)

        while i < n and j < n:
            # move zeroes to end of array by swapping values
            # nums[j] should not be 0 if we swap
            if nums[i] == 0 and nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1

            elif nums[i] != 0:
                i += 1
            j += 1
        return nums

S = Solution()

n1 = [0,1,0,3,12]

print(S.moveZeroes(n1)) # [1,3,12,0,0]