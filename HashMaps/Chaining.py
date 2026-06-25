class HashTable:

    def __init__(self, maxx):
        self.Max = maxx
        self.arr = [[] for _ in range(self.Max)]

    def get_hash(self, key):
        sumOfAscii = 0

        for i in key:
            sumOfAscii += ord(i)

        return sumOfAscii % self.Max

    def placeInMap(self, key, val):
        h = self.get_hash(key)

        if len(self.arr[h]) != 0:
            self.arr[h].append((key, val))
        else:
            self.arr[h].append((key, val))

    def __setitem__(self, key, val):
        return self.placeInMap(key, val)

    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]

    def print(self):
        print(self.arr)


t = HashTable(100)

t["march 6"] = 200
t["march 109"] = 400



t.print()

