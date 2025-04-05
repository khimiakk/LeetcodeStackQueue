class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        count = 0
        probe = self.head
        while probe:
            count += 1
            probe = probe.next
        return count

    def isempty(self):
        return self.head is None

    def peek(self):
        if not self.isempty():
            return self.head.data
        return None

    def push(self, item):
        node = Node(item)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        return None


class MyStack(object):

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        return self.queue1.push(x)

    def pop(self):
        """
        :rtype: int
        """

        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())
        node = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return node

    def top(self):
        """
        :rtype: int
        """

        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())
        node = self.queue1.pop()
        self.queue2.push(node)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return node

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue1.isempty() and self.queue2.isempty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
