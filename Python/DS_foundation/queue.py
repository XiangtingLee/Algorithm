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
        index = self.front
        while index != self.rear:
            print(self.data[index])
            index = (index + 1) % len(self.data)

if __name__ == "__main__":
    seq_queue = SeqQueue(5)
    [seq_queue.enqueue(i) for i in range(4)]
    seq_queue.show()
    seq_queue.dequeue()
    seq_queue.dequeue()
    seq_queue.enqueue(555)
    seq_queue.show()