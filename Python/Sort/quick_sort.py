class QuickSort(object):

    def __init__(self, arr=None):
        self.arr = arr if arr else []
        self.all_scheme = ["bilateral loop", "unilateral loop"]
        self.__all_scheme_dict = {
            "bilateral loop": self._partition_v1,
            "unilateral loop": self._partition_v2
        }

    def _partition_v1(self, start_index, end_index, asc):
        """
        bilateral loop
        :param start_index: sort array start index
        :param end_index: sort array end index
        :param asc: whether to sort in ascending order
        :return: pivot index
        """
        pivot = self.arr[start_index]   # 第一个元素作为基准元素
        left = start_index              # 左指针
        right = end_index               # 右指针
        while left != right:
            while left < right and ((self.arr[right] > pivot and asc) or (self.arr[right] < pivot and not asc)):
                right -= 1              # 判断左右指针值大小和排序顺序，决定是否移动右指针
            while left < right and ((self.arr[left] <= pivot and asc) or (self.arr[left] >= pivot and not asc)):
                left += 1               # 判断左右指针值大小和排序顺序，决定是否移动左指针
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]           # 交换左右指针值
        self.arr[left], self.arr[start_index] = self.arr[start_index], self.arr[left]   # 交换基准元素位置
        return left                                                                     # 返回基准元素索引

    def _partition_v2(self, start_index, end_index, asc):
        """
        unilateral loop
        :param start_index: sort array start index
        :param end_index: sort array end index
        :param asc: whether to sort in ascending order
        :return: pivot index
        """
        pivot = self.arr[start_index]   # 第一个元素作为基准元素
        mark = start_index              # 与基准元素比较，大小的分界点
        for judge_index in range(start_index + 1, end_index + 1):
            if (self.arr[judge_index] < pivot and asc) or (self.arr[judge_index] > pivot and not asc):
                mark += 1              # 判断值大小和排序顺序，决定是否向右移动指针
                self.arr[mark], self.arr[judge_index] = self.arr[judge_index], self.arr[mark]   # 将值置于标记左侧
        self.arr[start_index], self.arr[mark] = self.arr[mark], self.arr[start_index]           # 交换基准元素位置
        return mark                                                                             # 返回基准元素索引

    def recursion_sort(self, start_index, end_index, asc=True, scheme=None):
        """
        recursive quick sort
        :param start_index: sort array start index
        :param end_index: sort array end index
        :param asc: whether to sort in ascending order
        :param scheme: sort scheme
        :return: None
        """
        _scheme = self.__all_scheme_dict.get(scheme)                        # 排序方式
        if not scheme or not _scheme:                                       # 默认排序方式
            _scheme = self._partition_v2
        if start_index >= end_index:                                        # 做右指针相等时
            return                                                          # 排序完毕，跳出
        pivot_index = _scheme(start_index, end_index, asc)                  # 获取基准元素索引
        self.recursion_sort(start_index, pivot_index - 1, asc, scheme)      # 排序基准元素左侧
        self.recursion_sort(pivot_index + 1, end_index, asc, scheme)        # 排序基准元素右侧

    def non_recursion_sort(self, start_index, end_index, asc=True, scheme=None):
        """
        non_recursive quick sort
        :param start_index: sort array start index
        :param end_index: sort array end index
        :param asc: whether to sort in ascending order
        :param scheme: sort scheme
        :return: None
        """
        _scheme = self.__all_scheme_dict.get(scheme)                        # 排序方式
        if not scheme or not _scheme:                                       # 默认排序方式
            _scheme = self._partition_v2
        sort_stack = []
        root = {"start_index": start_index, "end_index": end_index}
        sort_stack.append(root)
        while len(sort_stack) > 0:
            sort_node = sort_stack.pop()
            pivot_index = _scheme(sort_node.get("start_index"), sort_node.get("end_index"), asc)
            if sort_node.get("start_index") < pivot_index - 1:
                sort_stack.append({"start_index": start_index, "end_index": pivot_index - 1})
            if sort_node.get("end_index") > pivot_index + 1:
                sort_stack.append({"start_index": pivot_index + 1, "end_index": end_index})

    def show_result(self):
        """
        show sorted array
        :return: None
        """
        print(", ".join([str(i) for i in self.arr]))


if __name__ == "__main__":
    array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    quick_sort = QuickSort(array)

    quick_sort.non_recursion_sort(0, len(array) - 1, False)
    quick_sort.show_result()

    print("use default scheme: unilateral loop")
    quick_sort.recursion_sort(0, len(array) - 1)
    quick_sort.show_result()
    quick_sort.recursion_sort(0, len(array) - 1, False)
    quick_sort.show_result()

    for use_scheme in quick_sort.all_scheme:
        print("use scheme: " + use_scheme)
        quick_sort.recursion_sort(0, len(array) - 1, False, use_scheme)
        quick_sort.show_result()
        quick_sort.recursion_sort(0, len(array) - 1, True, use_scheme)
        quick_sort.show_result()
