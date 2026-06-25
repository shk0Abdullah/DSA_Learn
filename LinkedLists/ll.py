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
            yield(pointer.data)
            pointer = pointer.next

    # can we do stream traverse means every iteration return something easy to reuse gonna took help from llm
    # have learned about the next and yield 
    def streamTraverse(self):
        stream = self.traverse()
        while True:
            try:
                print(next(stream))
            except StopIteration:
                break
    # now we are able to use the stream logic for search to delete or insert nice 
    def deleteAtPoint(self, data):
        ...
    
    def search (self, data):
        stream = self.traverse() # -> generator 
        value  = next(stream)
        i = 0
        while True:
            try: 
                i=i+1

                if data == value:
                    print('Found')
                    break
                else:
                    value = next(stream)
            except Exception as e:
                print("Not Found")
                print(i)
                break

        


obj1 = LL()
obj1.insertAtHead(23)
obj1.insertAtHead(21)
obj1.insertAtHead(11)

obj1.traverse()
obj1.streamTraverse()

obj1.search(11)
obj1.search(23)
obj1.search(21)
obj1.search(1)

