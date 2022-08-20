
class Node:
    def __init__(self,data):
        self.data = data
        self.left_node = None
        self.right_node = None

class BinaryTree:
    def __init__(self):
        self.builder_count=-1

    def build_binary_tree(self, data):
        self.builder_count +=1
        if data[self.builder_count]== -1:
            return None
        node = Node(data[self.builder_count])
        node.left_node = self.build_binary_tree(data)
        node.right_node = self.build_binary_tree(data)
        return node
    
    def preorder_traversal(self, root_node):
        print(root_node.data)
        self.preorder_traversal(root_node.left_node) if root_node.left_node else None
        self.preorder_traversal(root_node.right_node) if root_node.right_node else None
    
    def inorder_traversal(self, root_node):
        self.inorder_traversal(root_node.left_node) if root_node.left_node else None
        print(root_node.data)
        self.inorder_traversal(root_node.right_node) if root_node.right_node else None
    
    def postorder_traversal(self, root_node):
        self.postorder_traversal(root_node.left_node) if root_node.left_node else None
        self.postorder_traversal(root_node.right_node) if root_node.right_node else None
        print(root_node.data)
    def level_order_traversal(self, root_node):
        pass
if __name__ == "__main__":
    input_data = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    root_node = tree.build_binary_tree(input_data)
    print(root_node.data)
    print("Preorder Traverse Started")
    tree.preorder_traversal(root_node)
    print("Inorder Traverse Started")
    tree.inorder_traversal(root_node)
    print("Postorder Traverse Started")
    tree.postorder_traversal(root_node)