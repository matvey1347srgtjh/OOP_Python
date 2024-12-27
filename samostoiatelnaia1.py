class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
       
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)

    def search(self, value):
        
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
       
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        return self._search_recursively(node.right, value)

    def delete(self, value):
        
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
       
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            
            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursively(node.right, min_larger_node.value)

        return node

    def _get_min(self, node):
       
        current = node
        while current.left is not None:
            current = current.left
        return current



bt = BinaryTree()


bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)


found_node = bt.search(7)
if found_node:
    print(f"Узел с значением {found_node.value} найден.")
else:
    print("Узел не найден.")


bt.delete(5)
deleted_node = bt.search(5)
if deleted_node:
    print(f"Узел с значением {deleted_node.value} найден.")
else:
    print("Узел успешно удален.")
