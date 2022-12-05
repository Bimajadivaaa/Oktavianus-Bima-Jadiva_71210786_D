class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            elif self.left is not None:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            elif self.right is not None:
                self.right.insert(data)
        else:
            return False
        return True
class BinaryTree:
    def __init__(self):
        self.root = Node(0,None)
    def add(self, data):
        if self.root.left is None and data%2 != 0:
            self.root.left = Node(data,self.root)
        elif self.root.right is None and data%2 == 0:
            self.root.right = Node(data,self.root)
        elif self.root.right is not None and data%2 != 0:
            if data % 2 != 0:
                self.root.left.insert(data)
            elif data % 2 == 0:
                self.root.right.insert(data)
    def sumGanjil(self,node,ganjil=[]):
        if node is not None:
            if node.data % 2 != 0:
                ganjil.append(node.data)
            self.sumGanjil(node.left,ganjil)
            self.sumGanjil(node.right,ganjil)
        return sum(ganjil)
    def hasilGanjil(self):
        return self.sumGanjil(self.root)
if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print()
    print("Penjumlahan data ganjil =",binaryT.hasilGanjil())