
class BinaryHeap(object):

    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.heap = arr

    def up_adjust(self, big_top=True):
        """
        operation of node up adjust
        :param big_top: is big heap
        :return: None
        """
        child_index = len(self.heap) - 1                                        # left_child_index = (parent_index*2)+1
        parent_index = (child_index - 1) // 2                                   # right_child_index = (parent_index*2)+2
        while child_index > 0 and (
                (self.heap[child_index] > self.heap[parent_index] and big_top) or
                (self.heap[child_index] < self.heap[parent_index] and not big_top)
        ):                                                                          # 当前节点与父节点不满足排序关系时
            self.heap[child_index] = self.heap[parent_index]                        # 父节点下移
            child_index = parent_index                                              # 修改被移动节点索引
            parent_index = (child_index - 1) // 2                                   # 继续向上寻找父节点

    def down_adjust(self, parent_index, length, big_top=True):
        """
        operation of node down adjust
        :param parent_index: parent node index
        :param length: heap length
        :param big_top: is big heap
        :return: None
        """
        child_index = (parent_index * 2) + 1
        while child_index < length:
            if child_index + 1 < length and (
                    (self.heap[child_index] < self.heap[child_index + 1] and big_top) or
                    (self.heap[child_index] > self.heap[child_index + 1] and not big_top)
            ):
                child_index += 1                                                            # 找到更大(或更小)的子节点
            if self.heap[parent_index] == self.heap[child_index] or (
                    (self.heap[parent_index] > self.heap[child_index] and big_top) or
                    (self.heap[parent_index] < self.heap[child_index] and not big_top)
            ):                                                                              # 判断父子节点的大小关系
                break                                                                       # 不符合排序规则直接跳出
            self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]  # 节点上移
            parent_index = child_index                                              # 当前被移动节点的索引改为右子节点的索引
            child_index = (child_index * 2) + 1                                     # 左子节点

    def build_heap(self, big_top=True):
        """
        build a heap
        :param big_top: is big heap
        :return: None
        """
        for parent_index in range((len(self.heap) - 2) // 2, -1, -1):
            self.down_adjust(parent_index, len(self.heap), big_top)

    def show_heap(self):
        """
        show a heap
        :return: None
        """
        print(",".join([str(i) for i in self.heap]))


if __name__ == "__main__":
    binary_big_top_heap = BinaryHeap([6, 8, 7, 5, 3, 1, 10, 2, 9])
    binary_big_top_heap.build_heap()
    binary_big_top_heap.show_heap()
    binary_small_top_heap = BinaryHeap([10, 7, 9, 8, 1, 4, 6, 3, 2])
    binary_small_top_heap.build_heap(False)
    binary_small_top_heap.show_heap()
