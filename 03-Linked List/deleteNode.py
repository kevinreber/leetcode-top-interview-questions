''' 237. Delete Node in a Linked List

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Example 3:
    Input: head = [1,2,3,4], node = 3
    Output: [1,2,4]

Example 4:
    Input: head = [0,1], node = 0
    Output: [1]

Example 5:
    Input: head = [-3,5,-99], node = -3
Output: [5,-99]
 
Constraints:
    - The number of the nodes in the given list is in the range [2, 1000].
    - -1000 <= Node.val <= 1000
    - The value of each node in the list is unique.
    - The node to be deleted is in the list and is not a tail node
'''

''' ***IF HEAD IS GIVEN*** '''
# def deleteNode(head, val):
#     cur = head

#     while cur.next:
#         next_node = cur.next

#         # if cur.val == val:


#         # if next node == val, remove next node
#         if next_node.val == val:
#             # if no cur.next.next, cur.next = None
#             if not cur.next.next:
#                 cur.next = None
#             else:    
#                 cur.next = cur.next.next
#         cur = cur.next

#     return head

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

def printList(head):
    '''Prints out a Linked List as an array'''
    cur = head
    values = []
    while cur:
        values.append(cur.val)
        cur = cur.next

    return values

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# List Node Test 1
L1 = ListNode(4)
L1.next = ListNode(5)
L1.next.next = ListNode(1)
L1.next.next.next = ListNode(9)

# List Node Test 2
L2 = ListNode(4)
L2.next = ListNode(5)
L2.next.next = ListNode(1)
L2.next.next.next = ListNode(9)

# List Node Test 3
L3 = ListNode(0)
L3.next = ListNode(1)

# List Node Test 4
L4 = ListNode(-3)
L4.next = ListNode(5)
L4.next.next = ListNode(-99)

# D1 = deleteNode(L1, 5)
# D2 = deleteNode(L2, 1)
# D3 = deleteNode(L3, 0)
# D4 = deleteNode(L4, -3)

deleteNode(L1.next)
deleteNode(L2.next.next)
deleteNode(L3)
deleteNode(L4)

# print(printList(D1)) # [4, 1, 9]
# print(printList(D2)) # [4, 5, 9]
# print(printList(D3)) # [1]
# print(printList(D4)) # [5, -99]

print(printList(L1)) # [4, 1, 9]
print(printList(L2)) # [4, 5, 9]
print(printList(L3)) # [1]
print(printList(L4)) # [5, -99]
