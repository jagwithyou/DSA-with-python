class HashTable:
    def __init__(self, max):
        self.MAX = max
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    def __setitem__(self, key, value):
        key_hash = self.get_hash(key)
        key_available = False
        for idx, element in enumerate(self.arr[key_hash]):
            print(element)
            if element[0] == key:
                self.arr[key_hash][idx] = (key,value)
        if not key_available:
            self.arr[key_hash].append((key,value))
    
    def __getitem__(self, key):
        key_hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[key_hash]):
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        key_hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[key_hash]):
            print(element)
            if element[0] == key:
                del self.arr[key_hash][idx]
        
if __name__ == "__main__":
    hash_table = HashTable(10)
    print(hash_table.get_hash("march 6"))
    print(hash_table.get_hash("march 17"))
    hash_table["march 6"]= 299
    print(hash_table["march 6"])
    hash_table["march 17"] = 400
    print(hash_table["march 6"])
    print(hash_table["march 17"])
    del hash_table["march 17"]
    print(hash_table["march 17"])