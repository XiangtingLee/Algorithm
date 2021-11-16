class MyArray(object):

    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def append(self, item):
        """
        尾插
        :param item:
        :return:
        """
        if self.size >= len(self.array):
            self.resize()
        self.array[self.size] = item
        self.size += 1

    def insert(self, index, element):
        """
        普通的插入
        :param index:
        :param element:
        :return:
        """
        if not 0 <= index <= self.size:
            raise IndexError("out of index")            # 下标越界

        for i in range(self.size - 1, index - 1, -1):   # 下标没有越界
            self.array[i + 1] = self.array[i]           # 从右向左逐个移动一个位置

        self.array[index] = element     # 插入元素
        self.size += 1                  # 数组长度+1

    def insert_v2(self, index, element):
        """
        带自动扩容的插入
        :param index:
        :param element:
        :return:
        """
        if not 0 <= index <= self.size:
            raise IndexError("out of index")    # 下标越界

        if self.size >= len(self.array):        # 当前数组容量已满
            self.resize()                       # 先扩容
        self.insert(index, element)             # 再插入

    def resize(self):
        """
        数组扩容
        :return:
        """
        new_arr = [None] * len(self.array)
        self.array += new_arr

    def output(self):
        print(",".join(str(self.array[i]) for i in range(self.size)))

    def remove(self, index):
        if not 0 <= index < self.size:
            raise IndexError("out of index")
        for index in range(index, self.size - 1):
            self.array[index] = self.array[index+1]
        self.size -= 1

    def pop(self):
        if self.size <= 0:
            raise IndexError("pop from empty array")
        item = self.array[self.size]
        self.size -= 1
        return item




if __name__ == "__main__":
    arr = MyArray(2)
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.output()
    print(f"arr mem length：{len(arr.array)}\narr data length：{arr.size}\n")


    arr1 = MyArray(3)
    arr1.insert(0, 10)
    arr1.insert(0, 11)
    arr1.insert(0, 12)
    arr1.output()
    print(f"arr1 mem length：{len(arr1.array)}\narr1 data length：{arr1.size}\n")

    arr2 = MyArray(2)
    arr2.insert_v2(0, 20)
    arr2.insert_v2(0, 21)
    arr2.insert_v2(0, 22)
    arr2.output()
    print(f"arr2 mem length：{len(arr2.array)}\narr2 data length：{arr2.size}\n")
    arr2.remove(1)
    arr2.output()
    print(f"arr2 mem length：{len(arr2.array)}\narr2 data length：{arr2.size}\n")

    pop_item = arr2.pop()
    print(f"arr2 pop：{pop_item}")
    arr2.output()
    print(f"arr2 mem length：{len(arr2.array)}\narr2 data length：{arr2.size}\n")
