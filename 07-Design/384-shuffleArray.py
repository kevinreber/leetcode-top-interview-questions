''' 384. Shuffle and Array

Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:
    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.
    
Example 1:
    Input
        ["Solution", "shuffle", "reset", "shuffle"]
        [[[1, 2, 3]], [], [], []]
    Output
        [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
    Solution solution = new Solution([1, 2, 3]);
    solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
    solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
    solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

Constraints:
    1 <= nums.length <= 200
    -106 <= nums[i] <= 106
    All the elements of nums are unique.
    At most 5 * 104 calls will be made to reset and shuffle.
'''
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
    
    '''Solution 2'''
    def shuffle(self):
        aux = list(self.nums)

        for idx in range(len(self.nums)):
            remove_idx = random.randrange(len(aux))
            self.nums[idx] = aux.pop(remove_idx)

        return self.nums

    '''Solution 1'''
    # def shuffle(self):
    #     """
    #     Returns a random shuffling of the array.
    #     :rtype: List[int]
    #     """
    #     n = len(self.nums)
    #     # make new list for shuggled integers
    #     shuffled_nums = [0 for i in range(0, n)]
        
    #     # will be used as reference to ensure
    #     # no elements have the same index
    #     new_positions = set()
        
    #     for i in range(n):
    #         # current number in self.nums
    #         num = self.nums[i]
            
    #         # create new random index integer
    #         new_position = randint(0, n - 1)
            
    #         # if new_position is already in new_positions
    #         # get a new random integer
    #         while new_position in new_positions:
    #             new_position = randint(0, n - 1)
            
    #         new_positions.add(new_position)
            
    #         # if new_position is unique
    #         # add number into shuffled_nums
    #         shuffled_nums[new_position] = num
                
    #     return shuffled_nums

        