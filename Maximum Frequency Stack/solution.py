from collections import defaultdict

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

class FreqStack(object):

    def __init__(self):
        self.stack = defaultdict(Stack)
        self.freq = defaultdict(int)
        self.f_max = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        self.freq[val] += 1
        curr_freq = self.freq[val]
        if curr_freq > self.f_max:
            self.f_max = curr_freq
        self.stack[curr_freq].push(val)

    def pop(self):
        """
        :rtype: int
        """

        val = self.stack[self.f_max].pop()
        self.freq[val] -= 1
        if self.stack[self.f_max].isempty():
            self.f_max -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
