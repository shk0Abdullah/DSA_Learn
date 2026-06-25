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
            yield(pointer)
            pointer = pointer.next

    # can we do stream traverse means every iteration return something easy to reuse gonna took help from llm
    # have learned about the next and yield 
    def streamTraverse(self):
        stream = self.traverse()
        while True:
            try:
                print(next(stream).data)
            except StopIteration:
                break
    # now we are able to use the stream logic for search to delete or insert nice 
    def ChangeAtPoint(self, data, updatedData):
        stream  = self.traverse() 
        value = next(stream)
        while True:
            try:
                if data == value.data:
                    print("Found")
                    self.head.data = updatedData
                    print("Updated")
                    break
                else:
                    value = next(stream)
            except Exception as e: 
                print("NOT FOUND", e)
                break
    def DeleteAtPoint(self, data):
        stream  = self.traverse() 
        value = next(stream)
        pointer = value
        while True:
            try: 
                if pointer.data == data:
                    self.head = value.next
                    break
                elif pointer.next.data == data: 
                    value.next = value.next.next
                else:
                    pointer = next(stream)
            except Exception as e:
                print("Not Found")
                break
       


       


    def search (self, data):
        stream = self.traverse() # -> generator 
        value  = next(stream)
        i = 0
        while True:
            try: 
                i=i+1

                if data == value.data:
                    print('Found')
                    break
                else:
                    value = next(stream)
            except Exception as e:
                print("Not Found")
                print(i)
                break

    def Length(self):
        l = 0 
        pointer = self.head
        print(self.head)
        while pointer:
            l = l+1 
            pointer = pointer.next
        print(l)


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

print("Updated")
obj1.ChangeAtPoint(11,10)
obj1.streamTraverse()

print("DEL")
# obj1.DeleteAtPoint(21)
# obj1.DeleteAtPoint(10)
# obj1.DeleteAtPoint(23)

obj1.streamTraverse()

obj1.Length()