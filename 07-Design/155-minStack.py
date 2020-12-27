''' 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example 1:
    Input
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

    Output
        [null,null,null,null,-3,null,0,-2]

Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    
Constraints:
    Methods pop, top and getMin operations will always be called on non-empty stacks.
'''

class MinStack(object):

    def __init__(self):
        '''Initialize data structure'''
        self.stack = []
        # second stack will hold our getMin value
        # so we have access to our min value at constant time O(1)
        self.min_stack = []
    
    def push(self, x):
        self.stack.append(x)

        # check to see if we need to update minimum value
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        # if last element in min_stack == last element in stack, remove last element in min_stack
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

ms1 = MinStack()
ms1.push(-2)
ms1.push(0)
ms1.push(-3)
print(ms1.getMin()) # -3
ms1.pop()
print(ms1.top()) # 0
print(ms1.getMin()) # -2
