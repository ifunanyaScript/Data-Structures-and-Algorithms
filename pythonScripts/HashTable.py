# Separate Chaining Hash Table.
class HashTable1:
    def __init__(self):
        self.max = 10
        self.array = [[] for i in range(self.max)]
    
    def getIndex(self, key):
        hash = 0
        for character in key:
            hash += ord(character)
        i = hash % self.max
        return i
    
    def __setitem__(self, key, value):
        i = self.getIndex(key)
        found = False
        for index, pair in enumerate(self.array[i]):
            if len(pair)==2 and pair[0]==key:
                self.array[i][index] = (key, value)
                found = True
                break
        if not found:
            self.array[i].append((key, value))
    
    
    def __getitem__(self, key):
        i = self.getIndex(key)
        for pair in self.array[i]:
            if pair[0] == key:
                return pair[1]
    
    def __delitem__(self, key):
        i = self.getIndex(key)
        for index, pair in enumerate(self.array[i]):
            if pair[0] == key:
                del self.array[i][index]



# Open Addressing(Linear Probing)
class HashTable2:  
    def __init__(self):
        self.max = 10
        self.array = [None for i in range(self.max)]
        
    def getIndex(self, key):
        hash = 0
        for character in key:
            hash += ord(character)
        i = hash % self.max
        return i
    
    
    def probableIndices(self, index):
        return [*range(index, len(self.array))] + [*range(0,index)]
    
    
    def findSlot(self, key, index):
        indices = self.probableIndices(index)
        for idx in indices:
            if self.array[idx] is None:
                return idx
            if self.array[idx][0] == key:
                return idx
        raise Exception("This Hash map is full.")
    
    
    def __setitem__(self, key, value):
        i = self.getIndex(key)
        if self.array[i] is None:
            self.array[i] = (key,value)
        else:
            new_i = self.findSlot(key, i)
            self.array[new_i] = (key, value)
    
    
    def __getitem__(self, key):
        i = self.getIndex(key)
        if self.array[i] is None:
            return
        indices = self.probableIndices(i)
        for idx in indices:
            pair = self.array[idx]
            if pair is None:
                return
            if pair[0] == key:
                return pair[1]
    
        
    def __delitem__(self, key):
        i = self.getIndex(key)
        indices = self.probableIndices(i)
        for idx in indices:
            if self.array[idx] is None:
                return
            if self.array[idx][0] == key:
                self.array[idx] = None


if __name__ == '__main__':
    hT1 = HashTable1()
    hT1['Yesterday'] = 12
    hT1['Today'] = 24
    hT1['Tomorrow'] = 48
    hT1['Next week'] = 96
    hT1['Next month'] = 192
    print(f"{hT1['Yesterday'], hT1['Today'], hT1['Tomorrow']}")
    print(hT1.array)
    del hT1['Today']
    print(hT1.array)
    print('__________________________________')
    hT2 = HashTable2()
    hT2['Yesterday'] = 12
    hT2['Today'] = 24
    hT2['Tomorrow'] = 48
    hT2['Next week'] = 96
    hT2['Next month'] = 192
    print(f"{hT2['Yesterday'], hT2['Today'], hT2['Tomorrow']}")
    print(hT2.array)
    del hT2['Today']
    print(hT2.array)

# ifunanyaScript