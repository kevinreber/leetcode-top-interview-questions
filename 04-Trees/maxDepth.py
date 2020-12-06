''' 104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Example 3:
    Input: root = []
    Output: 0

Example 4:
    Input: root = [0]
    Output: 1
 
Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    # base case
    if not root:
        return 0

    '''Solution 1'''
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    if not root.left:
        return right + 1
    if not root.right:
        return left + 1

    return max(left, right) + 1

    '''Solution 2'''
    # return 1 + max(maxDepth(root.left), maxDepth(root.right)) 

tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

print(maxDepth(tree1)) # 3

tree2 = TreeNode(1)
tree2.right = TreeNode(2)

print(maxDepth(tree2)) # 2