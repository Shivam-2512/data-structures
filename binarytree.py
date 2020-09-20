#O(n) = O(log n )

class BinarySearchTree:
     def __init__(self, data):
         self.data = data
         self.left = None
         self.right = None

     def add_child(self, data):
         if data == self.data:
             return
         if data < self.data:
             if self.left:
                 self.left.add_child(data)
             else:
                 self.left = BinarySearchTree(data)

         else:
             if self.right:
                 self.right.add_child(data)
             else:
                 self.right = BinarySearchTree(data)

     def in_order_traversal(self):
         elements =[]

         #visit left tree first
         if self.left:
             elements += self.left.in_order_traversal()

        #visit base node
         elements.append(self.data)
         #visit right node
         if self.right:
            elements += self.right.in_order_traversal()

         return elements

     def pre_order_traversal(self):
         elements = [self.data]

         #now left tree
         if self.left:
             elements += self.left.pre_order_traversal()

         #then right part
         if self.right:
             elements += self.right.pre_order_traversal()

         return elements

     def post_order_traversal(self):
         elements = []
         if self.left:
             elements += self.left.post_order_traversal()
         if self.right:
             elements += self.right.post_order_traversal()

         elements.append(self.data)

         return elements

     def search(self, val):
         if self.data == val:
             return True
         if val < self.data:
             if self.left:
                 return self.left.search(val)
             else:
                 return False
         if val > self.data:
             if self.right:
                 return self.right.search(val)
             else:
                 return False

     def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()

     def find_max(self):
         if self.right is None:
             return self.data
         return self.right.find_max()

     def calculate_sum(self):
         left_sum = self.left.calculate_sum() if self.left else 0
         right_sum = self.right.calculate_sum() if self.right else 0
         return self.data + left_sum + right_sum

     def delete(self, val):
         if val < self.data:
             if self.left:
                 self.left = self.left.delete(val)
         elif val > self.data:
             if self.right:
                 self.right = self.right.delete(val)
         else:
             if self.left is None and self.right is None:
                 return None
             if self.left is None:
                 return self.right
             if self.right is None:
                 return self.left
             #min_val = self.right.find_min()
             #self.data = min_val
             #self.right.delete(min_val)
             max_val = self.left.find_max()
             self.data = max_val
             self.left.delete(max_val)

         return self




def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [7, 12, 14, 15, 20, 23, 27, 88]
    numbers_tree = build_tree(numbers)
    #print(numbers_tree.in_order_traversal())
    #print(numbers_tree.search(20))

    #s = ["a", "b", "c", "d"]
    #s_tree = build_tree(s)
    #print(s_tree.in_order_traversal())
    #print(s_tree.search("x"))
    #print(numbers_tree.find_min())
    #print(numbers_tree.find_max())
    #print(numbers_tree.calculate_sum())
    #print(numbers_tree.post_order_traversal())
    numbers_tree.delete(20)
    print("After deleting 20", numbers_tree.in_order_traversal())