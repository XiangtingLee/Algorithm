
class BubbleSort(object):

    def __init__(self, arr=None):
        self.arr = [] if not arr else arr

    def sort(self, asc=True):
        """
        base bubble sort
        :param asc: whether to sort in ascending order
        :return: None
        """
        for i in range(len(self.arr) - 1):
            for j in range(len(self.arr) - 1 - i):
                if (asc and self.arr[j] > self.arr[j + 1]) or (not asc and self.arr[j] < self.arr[j + 1]):
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    def sort_v2(self, asc=True):
        """
        improved bubble sort
        :param asc: whether to sort in ascending order
        :return: None
        """
        for i in range(len(self.arr) - 1):
            is_sorted = True                            # 有序标记，每一轮初始为True
            for j in range(len(self.arr) - 1 - i):
                if (asc and self.arr[j] > self.arr[j + 1]) or (not asc and self.arr[j] < self.arr[j + 1]):
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    is_sorted = False                   # 产生次序交换，说明不是有序
            if is_sorted:                               # 此轮未发生次序交换，说明剩下的序列为有序
                break

    def sort_v3(self, asc=True):
        """
        final improved bubble sort
        :param asc: whether to sort in ascending order
        :return: None
        """
        last_changed_index = 0                          # 记录最后一个交换的元素位置
        sort_border = len(self.arr) - 1                 # 记录无序比较的边界，比较到此即可
        for i in range(len(self.arr) - 1):
            is_sorted = True
            for j in range(sort_border):
                if (asc and self.arr[j] > self.arr[j + 1]) or (not asc and self.arr[j] < self.arr[j + 1]):
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    is_sorted = False                   # 产生次序交换，说明不是有序
                    last_changed_index = j              # 无序数列边界修改为最后一次交换位置的地方
            sort_border = last_changed_index
            if is_sorted:
                break

    def show_result(self):
        """
        show sorted array
        :return: None
        """
        print(", ".join([str(i) for i in self.arr]))


if __name__ == "__main__":
    bubble_sort = BubbleSort([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
    bubble_sort.sort()
    bubble_sort.show_result()
    bubble_sort.sort_v2()
    bubble_sort.show_result()
    bubble_sort.sort_v3()
    bubble_sort.show_result()
