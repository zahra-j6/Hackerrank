#https://leetcode.com/problems/implement-stack-using-queues/submissions/
class MyStack(object):
    q=[]
    length=0

    def __init__(self):
        self.q=[]
        self.length=0
        
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        self.q.append(x)
        self.length=self.length+1
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        val=self.q[self.length-1]
        self.q.remove(val)
        self.length=self.length-1
        return val
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        

    def top(self):
        return self.q[self.length-1]
        """
        Get the top element.
        :rtype: int
        """
        

    def empty(self):
        if self.length==0:
            return True
        else:
            return False
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
