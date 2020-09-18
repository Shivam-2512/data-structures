class Treenode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self,property_name):
        if property_name == 'both':
            val = self.name + "("+ self.designation +")"
        elif property_name == 'name':
            val = self.name
        else:
            val = self.designation

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + val)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def management():

    infra = Treenode("Vishwa", "Infrastructure Head")
    infra.add_child(Treenode("Dhaval", "cloud manager"))
    infra.add_child(Treenode("Abhijit", "App manager"))


    cto = Treenode("Chinmay", "CTO")
    cto.add_child(Treenode("Aamir", "Application Head"))
    cto.add_child(infra)



    hr = Treenode("Gels", "HR head")
    hr.add_child(Treenode("Peter", "Reqruitment Head"))
    hr.add_child(Treenode("Waqas", "Policy manager"))

    ceo = Treenode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo

if __name__ == '__main__':
    root = management()
    root.print_tree("name")
    root.print_tree("both")
    root.print_tree("designation")
