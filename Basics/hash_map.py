class HashTable:
    def __init__(self, max):
        self.MAX = max
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    
    def add(self, key, value):
        key_hash = self.get_hash(key)
        self.arr[key_hash] = value
    
    def get(self, key):
        key_hash = self.get_hash(key)
        return self.arr[key_hash]

    def __setitem__(self, key, value):
        key_hash = self.get_hash(key)
        self.arr[key_hash] = value
    
    def __getitem__(self, key):
        key_hash = self.get_hash(key)
        return self.arr[key_hash]

    def __getitem__(self, key):
        key_hash = self.get_hash(key)
        return self.arr[key_hash]
    
    def __delitem__(self, key):
        key_hash = self.get_hash(key)
        self.arr[key_hash] = None
        
if __name__ == "__main__":
    hash_table = HashTable(100)
    print(hash_table.get_hash("march 6"))
    hash_table.add("march 6", 299)
    print(hash_table.get("march 6"))
    hash_table["march 7"] = 400
    print(hash_table["march 7"])
    del hash_table["march 7"]
    print(hash_table["march 7"])