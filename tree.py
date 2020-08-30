class Node:
    def __init__(self, left, data, right):
        self.data=data
        self.left=left
        self.right=right
        pass
    pass

class Tree:
    root:Node(None,None,None)
    def __init__(self):
        pass
    def makeNode(self, left, data, right):
        node=Node(left,data,right)
        return node
    def setRoot(self,Node):
        self.root=Node
        return self.root
    def getRoot(self):
        return self.root
    def inorder(self, node):
        if(node!=None):
            
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
            pass
        pass
    pass
    def preorder(self, node):
        if(node!=None):
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
            pass
        pass
    pass
    def postorder(self, node):
        if(node!=None):
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
            pass
        pass
    pass

t1=Tree()
n4=t1.makeNode(None, 4, None)
n5=t1.makeNode(None,5,None)
n2=t1.makeNode(n4,2,n5)
n3=t1.makeNode(None, 3, None)
n1=t1.makeNode(n2,1,n3);
t1.setRoot(n1)
print("inorder")
t1.inorder(n1)
print("preorder")
t1.preorder(n1)
print("postorder")
t1.postorder(n1)
