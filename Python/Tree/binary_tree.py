from Python.DS_foundation.queue import LinkQueue, LinkNode


class TreeNode(LinkNode):

    def __init__(self, data):
        super().__init__(data)
        self.left = None
        self.right = None


class StackTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = 0


class BinaryTree(object):

    def __init__(self):
        ...

    def create(self, input_list, with_stack=False):
        """
        create binary tree
        :param input_list:  tree node list
        :param with_stack:  use stack method
        :return:            root node
        """
        if not input_list or input_list is None:
            return None
        data = input_list.pop(0)
        if not data:
            return None
        new_node = StackTreeNode(data) if with_stack else TreeNode(data)
        new_node.left = self.create(input_list, with_stack)
        new_node.right = self.create(input_list, with_stack)
        return new_node

    def pre_order_traversal(self, node):
        """
        pre order traversal a binary tree
        :param node:    root node
        :return:        root node
        """
        if not node:
            return None
        print(node.data)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)
        return node

    def in_order_traversal(self, node):
        """
        in order traversal a binary tree
        :param node:    root node
        :return:        root node
        """
        if not node:
            return None
        self.in_order_traversal(node.left)
        print(node.data)
        self.in_order_traversal(node.right)
        return node

    def post_order_traversal(self, node):
        """
        post order traversal a binary tree
        :param node:    root node
        :return:        root node
        """
        if not node:
            return None
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.data)
        return node

    @staticmethod
    def pre_order_traversal_with_stack(node):
        """
        pre order traversal a binary tree
        :param node:    root node
        :return:
        """
        stack = []                                      # ?????????????????????
        while node is not None or len(stack) > 0:       # ????????????????????????1.?????????????????? 2.?????????????????????
            while node:                                 # ?????????????????????????????????
                print(node.data)                        # ??????????????????????????????
                stack.append(node)
                node = node.left
            if len(stack) > 0:                          # ?????????????????????????????????????????????????????????????????????????????????????????????????????????
                node = stack.pop()
                node = node.right

    @staticmethod
    def in_order_traversal_with_stack(node):
        """
        in order traversal a binary tree
        :param node:    root node
        :return:
        """
        stack = []
        while node is not None or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.data)
                node = node.right

    @staticmethod
    def post_order_traversal_with_stack(node):
        """
        post order traversal a binary tree
        :param node:    root node
        :return:
        """
        stack = []
        while node is not None or len(stack) > 0:
            while node:
                if node.visited == 0:       # ????????????????????????????????????
                    node.visited += 1       # ????????????+1
                    stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                if node.visited == 2:       # ?????????????????????(???-??????-???-??????-???), ????????????????????????????????????????????????
                    print(node.data)
                    node = None
                else:
                    node.visited += 1       # ???????????????????????????????????????????????????????????????????????????
                    stack.append(node)
                    node = node.right

    @staticmethod
    def BFS_traversal(node):
        """
        BFS traversal a binary tree
        :param node:    root node
        :return:
        """
        queue = LinkQueue()
        queue.enqueue(node)
        while not queue.empty():
            node = queue.dequeue()
            print(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


if __name__ == "__main__":
    binary_tree = BinaryTree()
    root_node = binary_tree.create([3, 2, 9, None, None, 10, None, None, 8, None, 4])
    print("BFS traversal:")
    binary_tree.BFS_traversal(root_node)
    print("pre order traversal:")
    binary_tree.pre_order_traversal(root_node)
    print("in order traversal:")
    binary_tree.in_order_traversal(root_node)
    print("post order traversal:")
    binary_tree.post_order_traversal(root_node)
    root_node_with_stack = binary_tree.create([3, 2, 9, None, None, 10, None, None, 8, None, 4], with_stack=True)
    print("pre order traversal with stack:")
    binary_tree.pre_order_traversal_with_stack(root_node_with_stack)
    print("in order traversal with stack:")
    binary_tree.in_order_traversal_with_stack(root_node_with_stack)
    print("post order traversal with stack:")
    binary_tree.post_order_traversal_with_stack(root_node_with_stack)
