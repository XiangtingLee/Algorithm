from Python.Tree.binary_heap import BinaryHeap


class HeapSort(BinaryHeap):

    def __init__(self, arr):
        super().__init__(arr)
        self.heaped = False                 # 标记当前堆是否已经构建完成
        self.__sort_order = None            # 统一排序顺序为升序/降序

    def build_heap(self, big_top=True):
        """
        overwrite heap build
        :param big_top: is big heap
        :return: None
        """
        for parent_index in range((len(self.heap) - 2) // 2, -1, -1):
            self.down_adjust(parent_index, len(self.heap), big_top)
        self.heaped = True                  # 标记当前堆已构建完毕
        self.__sort_order = big_top         # 标记当前堆为大顶堆/小顶堆（大顶堆结果为升序，小顶堆结果为降序）

    def sort(self):
        """
        heap sort
        :return: None
        """
        if not self.heaped:
            self.build_heap()                                           # 堆没有构建需要先构建堆，默认为大顶堆，排序结果为升序
        for i in range(len(self.heap) - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]     # 将堆顶放堆尾调换
            self.down_adjust(0, i, self.__sort_order)                   # 堆顶下沉找位置


if __name__ == "__main__":
    heap_sort = HeapSort([6, 8, 7, 5, 3, 1, 10, 2, 9])
    heap_sort.build_heap()
    heap_sort.show_heap()
    heap_sort.sort()
    heap_sort.show_heap()

