class HashTable:
    
    def  __init__ (self,maxx):
        self.Max = maxx
        self.arr = [None] * self.Max
    
    def get_hash(self,key):
        sumOfAscii = 0 
        for i in key:
            takeAscii = ord(i)
            sumOfAscii += takeAscii
        return sumOfAscii%self.Max
    
    def placeInMap(self, key, val):
        h = self.get_hash(key)
        i = 1
        while True:
            if self.arr[h] == None:
                self.arr[h] = val
                break
            else:
                if self.arr[h+i] == None:
                    self.arr[h+i] = val
                    break
                else:
                    i = i +1 

    def __setitem__(self, key, val):
        return self.placeInMap(key, val)

    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]

    def print(self):
        print(self.arr)
t = HashTable(100)
# they both have same index place and their values will collide so we will linearly increment the index by 
# considering the offset of that colliding index value and find a space to add the value
print (t.get_hash("march 6"))
print (t.get_hash("march 109"))

t["march 6"] = 202
t["march 109"] = 412
t.print()
