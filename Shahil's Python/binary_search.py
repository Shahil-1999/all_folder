class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None


    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)


    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")


    def preorder(self):
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()


    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end = " ")
        if self.rchild:
            self.rchild.inorder()


    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end = " ")

                

root = BST(10)
list = [6, 3, 1, 6, 98, 3, 7]
for i in list:
    root.insert(i)


# root = BST(10)
# n = map(int,input("Enter elements with space: ").split())
# for i in n:
#     root.insert(n)

print("preorder")
root.preorder()
print()
print("inorder")
root.inorder()
print()
print("postorder")
root.postorder()
