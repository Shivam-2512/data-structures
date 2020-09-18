class Treenode:
    def __init__(self, data):
        self.data = data
        self.children =[]
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):

        level = 0
        p = self.parent
        while p :
            level+=1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode("Laptop")
    laptop.add_child(Treenode("Mac"))
    laptop.add_child(Treenode("Dell"))
    laptop.add_child(Treenode("HP"))

    smartphones = Treenode("Smart Phones")
    smartphones.add_child(Treenode("Apple"))
    smartphones.add_child(Treenode("ASUS"))
    smartphones.add_child(Treenode("MI"))

    tv = Treenode("TV")
    tv.add_child(Treenode("SAMSUNG"))
    tv.add_child(Treenode("LG"))

    root.add_child(laptop)
    root.add_child(smartphones)
    root.add_child(tv)

    return root



if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    #print(root.get_level())
    pass