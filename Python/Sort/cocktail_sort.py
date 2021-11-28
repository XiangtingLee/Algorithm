class CocktailSort(object):

    def __init__(self, arr=None):
        self.arr = [] if not arr else arr

    def sort(self, asc=True):
        """
        base cocktail sort
        :param asc: whether to sort in ascending order
        :return: None
        """
        for i in range(len(self.arr) // 2):
            is_sorted = True
            for j in range(len(self.arr) - 1 - i):              # 奇数轮: 左 -> 右
                if (asc and self.arr[j] > self.arr[j + 1]) or (not asc and self.arr[j] < self.arr[j + 1]):
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    is_sorted = False
            if is_sorted:
                break

            is_sorted = True
            for j in range(len(self.arr) - 1 - i, i, -1):       # 偶数轮: 左 <- 右
                if (asc and self.arr[j] < self.arr[j - 1]) or (not asc and self.arr[j] > self.arr[j - 1]):
                    self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
                    is_sorted = False
            if is_sorted:
                break

    def show_result(self):
        """
        show sorted array
        :return: None
        """
        print(", ".join([str(i) for i in self.arr]))


if __name__ == "__main__":
    bubble_sort = CocktailSort([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
    bubble_sort.sort()
    bubble_sort.show_result()
