class Node:
    def __init__ (self, prev= None, data= None,Next=None,):
        self.next = Next
        self.data= data
        self.prev = prev

class DLL: 
    def __init__(self):
        self.head = None 
        self.tail = None

    def insertAtHead(self, data):
        if self.Length() == 0:
            node = Node(self.head,data,self.tail)
            self.head = node
            self.tail = node
        else:
            node = Node(Next = self.head ,data = data,prev= None)
            self.head.prev = node
            self.head = node
            
      
          


        
    def insertAtEnd(self,data):
        # we have to traverse to add it on the end or make the double pointer to reduce the complexity
        # LOL its started to getting tough
        if self.Length() == 0:
            self.head = Node(self.tail,data,self.head)
            self.head =node
            self.tail = node
        else:
            node = Node(self.tail, data, None)
            self.tail.next = node
            self.tail = node
            
    def FormatedTraversalFromHead(self):
        while self.head:
            print(f"{self.head.data}-> ", end="")
            self.head = self.head.next
        
    def FormatedTraversalFromTail(self):
        while self.tail:
            print(f"-> {self.tail.data}", end="")
            self.tail = self.tail.prev

    def Length(self):
        l = 0 
        pointer = self.head
        while pointer:
            l = l+1 
            pointer = pointer.next
        
        return(l)

obj1 = DLL()
obj1.insertAtHead(10)
obj1.insertAtHead(11)
obj1.insertAtEnd(23)


obj1.FormatedTraversalFromHead()
obj1.FormatedTraversalFromTail()

# should be 11 10

# should be 10 11