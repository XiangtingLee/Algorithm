class SeqStack(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.size = 0

    def pop(self):
        if self.size <= 0:
            raise IndexError("pop from empty stack!")
        self.size -= 1
        data = self.stack[self.size]
        self.stack[self.size] = None
        return data

    def push(self, data):
        if self.size >= self.capacity:
            raise IndexError("push to full stack!")
        self.stack[self.size] = data
        self.size += 1
        return True

    def show(self):
        [print("| {0:^6} |\n——————————".format(str(self.stack[i]))) for i in range(self.capacity - 1, -1, -1)]


class StackNode(object):

    def __init__(self):
        self.data = None
        self.next = None


class LinkStack(object):

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def get(self, index):
        if not 0 <= index < self.size:
            raise IndexError("out of index")
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def pop(self):
        if self.size <= 0:
            raise IndexError("pop from empty stack!")
        prev_node = self.get(self.size - 2)
        prev_node.next = None
        self.last = prev_node
        pop_node = prev_node.next
        self.size -= 1
        return pop_node

    def push(self, data):
        push_node = StackNode()
        push_node.data = data
        if self.size == 0:
            self.head = push_node
            self.last = push_node
        else:
            self.last.next = push_node
            self.last = push_node
        self.size += 1

    def show(self):
        p = self.head
        stack_list = []
        for i in range(self.size):
            stack_list.append("| {0:^6} |\n——————————".format(str(p.data)))
            p = p.next
        [print(i) for i in stack_list[::-1]]


if __name__ == "__main__":
    # 顺序栈
    seq_stack = SeqStack(5)
    [seq_stack.push(i) for i in range(4, 0, -1)]
    # seq_stack.show()
    seq_stack.pop()
    seq_stack.show()

    # 链栈
    link_stack = LinkStack()
    [link_stack.push(i) for i in range(5, 0, -1)]
    # link_stack.show()
    link_stack.pop()
    link_stack.show()
