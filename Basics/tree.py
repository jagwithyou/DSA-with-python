class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        count = 0
        iterator = self
        while iterator:
            count+=1
            iterator = iterator.parent
        return count
        
    def print_Tree(self):
        prefix = (" "* self.get_level()*2) + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_Tree()
    

def build_tree():
    root_node = Tree("Electronics")

    mobile_node = Tree("Mobile")
    mobile_node.add_child(Tree("Samsung"))
    mobile_node.add_child(Tree("Apple"))
    mobile_node.add_child(Tree("Lenovo"))

    tv_node = Tree("TV")
    tv_node.add_child(Tree("MI"))
    tv_node.add_child(Tree("Onida"))

    root_node.add_child(mobile_node)
    root_node.add_child(tv_node)

    return root_node


if __name__ == "__main__":
    root = build_tree()
    root.print_Tree()
    # print(root.data)