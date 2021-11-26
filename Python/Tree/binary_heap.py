
class BinaryHeap(object):

    def __init__(self, arr=None):
        self.heap = arr

    def up_adjust(self):
        child_index = len(self.heap) - 1                                        # left_child_index = (parent_index*2)+1
        parent_index = (child_index - 1) // 2                                   # right_child_index = (parent_index*2)+2
        cache_child_item = self.heap[child_index]                               # 缓存移动的节点
        while child_index > 0 and cache_child_item < self.heap[parent_index]:   # 当前节点小于父节点时
            self.heap[child_index] = self.heap[parent_index]                    # 父节点下移
            child_index = parent_index                                          # 当前被移动节点的索引修改为父节点的索引
            parent_index = (child_index - 1) // 2                               # 继续向上寻找父节点
        self.heap[child_index] = cache_child_item                               # 当前节点大于父节点时不上浮，将节点置于此

    def down_adjust(self, parent_index, length):
        child_index = (parent_index * 2) + 1
        cache_parent_item = self.heap[parent_index]
        while child_index < length:
            if child_index + 1 < length and self.heap[child_index] > self.heap[child_index + 1]:
                child_index += 1                                        # 如果右子节点更小，定位到右子节点
            if cache_parent_item <= self.heap[child_index]:             # 如果父节点小于任何子节点
                break                                                   # 直接跳出
            self.heap[parent_index] = self.heap[child_index]            # 右子节点上移
            parent_index = child_index                                  # 当前被移动节点的索引修改为右子节点的索引
            child_index = (child_index * 2) + 1                         # 左子节点
        self.heap[parent_index] = cache_parent_item

    def build_heap(self):
        for parent_index in range((len(self.heap) - 2) // 2, -1, -1):
            self.down_adjust(parent_index, len(self.heap))

    def show_heap(self):
        print(",".join([str(i) for i in self.heap]))


if __name__ == "__main__":
    binary_heap = BinaryHeap([6, 8, 7, 5, 3, 1, 10, 2, 9])
    binary_heap.build_heap()
    binary_heap.show_heap()
