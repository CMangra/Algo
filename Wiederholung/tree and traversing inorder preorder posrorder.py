class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def find_val(self, val):
        if val < self.data:
            if self.left is None:
                return False
            return self.left.find_val(val)
        elif val > self.data:
            if self.right is None:
                return False
            return self.right.find_val(val)
        else: 
            return True

    #inorder
    def print_inorder(self):
        
        if self.left:
            self.left.print_inorder()
            
        print(self.data)
        
        if self.right:
            self.right.print_inorder()
            
    def print_preorder(self):
        print(self.data)
        
        if self.left:
            self.left.print_preorder()
        
        if self.right:
            self.right.print_preorder()
    
    def print_postorder(self):
        
        if self.left:
            self.left.print_postorder()
        
        if self.right:
            self.right.print_postorder()
            
        print(self.data)

root = Node('F')

for v in 'BADCEGIH':
    root.insert(v)

print(root)#root exists
print(root.left)#root has a left object
print(root.right)#root has a right object

print("This is the element at the left of the root: "+root.left.data)#the data at the left of root

print(root.print_inorder())

print("Finding A: ")
print(root.find_val('A'))

print("Finding B: ") 
print(root.find_val('B'))

print("Finding X: ") 
print(root.find_val('X'))

print("Finding 4: ") 
print(root.find_val(4)) # return exception because 4 is an integer and integer cannot be compared to strings


