from Python.Tree.binary_heap import BinaryHeap


class PriorityQueue(BinaryHeap):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = len(self.heap)

    def enqueue(self, elem):
        """
        enqueue an item
        :param elem: item for enqueue
        :return: None
        """
        self.heap.append(elem)                  # 新元素添加到最有一个叶子节点后
        self.size += 1                          # 队列数量变化
        self.up_adjust()                        # 新元素上浮找到合适位置

    def dequeue(self):
        """
        dequeue an item
        :return: item of dequeue
        """
        if self.size <= 0:
            raise IndexError("can not dequeue from a null queue!")
        head = self.heap[0]                     # 堆顶出队
        self.heap[0] = self.heap.pop()          # 最后一个节点替换堆顶
        self.size -= 1                          # 队列数量变化
        self.down_adjust(0, self.size)          # 堆顶下沉找合适的位置
        return head                             # 返回出队item


if __name__ == "__main__":
    priority_queue = PriorityQueue([10, 7, 9, 8, 1, 4, 6, 3, 2])
    priority_queue.build_heap()
    priority_queue.show_heap()
    priority_queue.enqueue(5)
    priority_queue.show_heap()
    dequeue_item = priority_queue.dequeue()
    print(dequeue_item)
    priority_queue.show_heap()
