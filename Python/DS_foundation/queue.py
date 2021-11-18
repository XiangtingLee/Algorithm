class SeqQueue(object):
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if (self.rear + 1) % len(self.data) == self.front:  # 队列已满
            raise Exception("can not enqueue a full queue")
        self.data[self.rear] = data
        self.rear = (self.rear + 1) % len(self.data)

    def dequeue(self):
        if self.rear == self.front:
            raise Exception("can not dequeue a empty queue")
        item = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        return item

    def show(self):
        data = []
        index = self.front
        while index != self.rear:
            data.append(str(self.data[index]))
            index = (index + 1) % len(self.data)
        print(",".join(data))


class LinkNode(object):

    def __init__(self):
        self.data = None
        self.next = None


class LinkQueue(object):

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = LinkNode()
        new_node.data = data
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            raise Exception("can not dequeue a empty queue")
        data = self.front.data
        self.front = self.front.next
        return data

    def show(self):
        data = []
        node = self.front
        while node:
            data.append(str(node.data))
            node = node.next
        print(",".join(data))


if __name__ == "__main__":
    seq_queue = SeqQueue(5)
    print("full seq queue: ")
    [seq_queue.enqueue(i) for i in range(4)]
    seq_queue.show()
    print("dequeue 2 item: ")
    seq_queue.dequeue()
    seq_queue.dequeue()
    seq_queue.show()
    print()
    link_queue = LinkQueue()
    print("full link queue: ")
    [link_queue.enqueue(i) for i in range(6)]
    link_queue.show()
    print("dequeue 3 item: ")
    link_queue.dequeue()
    link_queue.dequeue()
    link_queue.dequeue()
    link_queue.show()
