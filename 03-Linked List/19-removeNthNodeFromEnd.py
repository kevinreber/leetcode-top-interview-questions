''' 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
 
Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.getLength(head)
        idx = 0
        curr = head
        prev = None

        while length - idx != n:
            prev = curr
            curr = curr.next
            idx+= 1
        
        # Base Case: if only one Node is passed
        if prev == None:
            head = curr.next
        else:
            prev.next = curr.next
            del curr.next

        # return (curr.val, prev.val)
        return self.showListValues(head)

    def getLength(self, head):
        curr=head
        idx = 0
        while curr:
            idx += 1
            curr=curr.next
        return idx

    def showListValues(self, head):
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr=curr.next
        return vals

# Test Cases
S = Solution()

L1 = ListNode(1)
L1.next = ListNode(2)
L1.next.next = ListNode(3)
L1.next.next.next = ListNode(4)
L1.next.next.next.next = ListNode(5)

print(S.removeNthFromEnd(L1, 2)) # [1,2,3,5]

L2 = ListNode(1)

print(S.removeNthFromEnd(L2, 1)) # []

L3 = ListNode(1)
L3.next = ListNode(2)
print(S.removeNthFromEnd(L3, 1)) # [1]
