class Node:
    def __init__ (self, Next= None, data= None,prev=None,):
        self.next = Next
        self.data= data
        self.prev = prev

class DLL: 
    def __init__(self):
        self.head = None 
        self.tail = None

    def insertAtHead(self, data):
        self.head = Node(self.head,data,self.tail)
    def insertAtEnd(self,data):
        # we have to traverse to add it on the end or make the double pointer to reduce the complexity
        # LOL its started to getting tough
        self.tail = Node(self.head, data, self.tail)
    def FormatedTraversalFromHead(self):
        while self.head:
            print(f"{self.head.data}-> ", end="")
            self.head = self.head.next
        print("None", end= "")

obj1 = DLL()
obj1.insertAtHead(10)
obj1.insertAtHead(11)
obj1.FormatedTraversal()
# should be 11 10