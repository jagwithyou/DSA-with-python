class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def add_child(self, data):
        if data < self.data:
            if self.left_child:
                self.left_child.add_child(data)
            else:
                self.left_child = BinaryTree(data)
        else:
            if self.right_child:
                self.right_child.add_child(data)
            else:
                self.right_child = BinaryTree(data)
    
    def inorder_traversal(self):
        elements = []
        if self.left_child:
            elements += self.left_child.inorder_traversal()
        elements.append(self.data)
        if self.right_child:
            elements += self.right_child.inorder_traversal()
        return elements

    def search(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left_child:
                return self.left_child.search(data)
            else:
                return False
        elif data > self.data:
            if self.right_child:
                return self.right_child.search(data)
            else:
                return False

    def find_min(self):
        if self.left_child:
            return self.left_child.find_min()
        else:
            return self.data
    
    def find_max(self):
        if self.right_child:
            return self.right_child.find_max()
        else:
            return self.data
    
    def delete(self, val):
        if val < self.data:
            if self.left_child:
                self.left_child = self.left_child.delete(val)
        elif val > self.data:
            if self.right_child:
                self.right_child = self.right_child.delete(val)
        else:
            if self.left_child is None and self.right_child is None:
                return None
            elif self.left_child is None:
                return self.right_child
            elif self.right_child is None:
                return self.left_child

            min_val = self.right_child.find_min()
            self.data = min_val
            self.right_child = self.right_child.delete(min_val)

        return self        

        
def build_tree(data):
    root_node = BinaryTree(data[0])
    for value in data[1:]:
        root_node.add_child(value)
    return root_node

if __name__ == "__main__":
    data = [5,3,4,1,2,6,7,8,9,0]
    tree = build_tree(data)
    print(tree.inorder_traversal())
    tree.delete(6)
    print(tree.inorder_traversal())
    # data = [17,4,1,20,9,23,18,34]
    # tree = build_tree(data)
    # print(tree.data)
    # print(tree.left_child.data)
    # print(tree.inorder_traversal())
    # print(tree.search(8))
    # print(tree.find_min())
    # print(tree.find_max())
    # tree.delete_element(20)
    # print(tree.inorder_traversal())

