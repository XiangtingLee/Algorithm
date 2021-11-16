class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList(object):

    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def get(self, index):
        if not 0 <= index < self.size:
            raise IndexError("out of index")
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, data, index=0):
        if not 0 <= index <= self.size:
            raise IndexError("out of index")
        node = Node(data)
        if self.size == 0:
            # 空链表插入
            self.head = node
            self.last = node
        elif index == 0:
            # 头插
            node.next = self.head
            self.head = node
        elif index == self.size:
            # 尾插
            self.last.next = node
            self.last = node
        else:
            # 中间插
            prev_node = self.get(index - 1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    def remove(self, index):
        if not 0 <= index < self.size:
            raise IndexError("out of index")
        if index == 0:
            if not self.size:
                raise IndexError("list is null")
            rm_node = self.head
            self.head = rm_node.next
        elif index == self.size - 1:
            prev_node = self.get(index - 1)
            rm_node = prev_node.next
            prev_node.next = None
            self.last = prev_node
        else:
            prev_node = self.get(index - 1)
            next_node = prev_node.next.next
            rm_node = prev_node.next
            prev_node.next = next_node
        self.size -= 1
        return rm_node

    def output(self):
        p = self.head
        while p:
            print("%s, " % p.data)
            p = p.next


if __name__ == "__main__":
    link_list = LinkList()
    for i in range(9, -1, -1):
        link_list.insert(i)
    link_list.insert(999, 2)
    link_list.remove(5)
    link_list.output()
