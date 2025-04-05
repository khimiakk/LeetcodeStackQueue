class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        self.head = Node(item, self.head)

    def peek(self):
        if self.isempty():
            return None
        return self.head.data

    def pop(self):
        if self.isempty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def isempty(self):
        return self.head is None

    def size(self):
        count = 0
        probe = self.head
        while probe:
            count += 1
            probe = probe.next
        return count

class MyQueue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stack1.push(x)

    def pop(self):
        """
        :rtype: int
        """

        if self.stack2.isempty():
            while not self.stack1.isempty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """

        if self.stack2.isempty():
            while not self.stack1.isempty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack1.isempty() and self.stack2.isempty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
