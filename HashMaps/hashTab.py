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
        self.arr[h] = val
    def __setitem__(self, key, val):
        return self.placeInMap(key, val)

    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]

    def print(self):
        print(self.arr)
t = HashTable(100)
t["march"] = 200
t.print()
print (t["march"])
