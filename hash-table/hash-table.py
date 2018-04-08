from numpy.random import randint

class HashTable():
    def __init__(self, size):
        self.size = size
        self.table = [[]] * size
    
    def _hash_function(self, key):
        if type(key) == int:
            return key % self.size
        elif type(key) == str:
            return ord(key) % self.size
        else:
            raise ValueError("unsupported key type (%s)" % (type(key)))
    
    def insert(self, key, value):
        index = self._hash_function(key)
        entries = self.table[index]
        if not entries:
            self.table[index].append((key, value))
            return
        for i in range(len(entries)):
            if entries[i] == key:
                self.table[index][i][1] = value

    def get(self, key):
        index = self._hash_function(key)
        entries = self.table[index]
        for entry in entries:
            if entry[0] == key:
                return entry[1]
        raise KeyError("key %s not found" % (str(key)))

    def remove(self, key):
        index = self._hash_function(key)
        entries = self.table[index]
        for i in range(len(entries)):
            if entries[i][0] == key:
                self.table[index].pop(i)
                return
        raise KeyError("key %s not found" % (str(key)))


def main():
    size = 200
    data = zip(list(randint(200, size=size)), list(randint(200, size=size)))
    
    table = HashTable(size)

    for datum in data:
        table.insert(int(datum[0]), datum[1])

    for datum in data:
        value = table.get(int(datum[0]))
        assert value == datum[1]

    print("completed")
    

if __name__ == "__main__":
    main()