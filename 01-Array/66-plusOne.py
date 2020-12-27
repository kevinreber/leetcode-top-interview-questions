''' 66. Plus One - Easy

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
 
Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

Example 3:
    Input: digits = [0]
    Output: [1]

Constraints:
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits str
        digits = [str(num) for num in digits]

        # join nums together and convert to integer
        digits = ''.join(digits)
        nums = int(digits)

        # add one
        nums += 1

        # convert to string
        nums = str(nums)

        # split each character and convert back to integer
        digits = [int(num) for num in nums]

        return digits

n1 = [1,2,3]
n2 = [4,3,2,1]
n3 = [0]

S = Solution()
print(S.plusOne(n1)) # [1,2,4]
print(S.plusOne(n2)) # [4,3,2,2]
print(S.plusOne(n3)) # [1]