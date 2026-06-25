class Node:
    def __init__ (self, data= None, Next = None):
        self.data= data
        self.next = Next

# if you are seeing have written all by myself feels good
class LL: 
    def __init__(self):
        self.head = None 
        # initially there is no head 

    def insertAtHead(self, data):
        self.head = Node(data,self.head)

    def traverse(self):
        pointer = self.head
        while pointer != None:
            print(pointer.data)
            pointer = pointer.next
    


obj1 = LL()
obj1.insertAtHead(23)
obj1.insertAtHead(21)
obj1.insertAtHead(11)

obj1.traverse()
