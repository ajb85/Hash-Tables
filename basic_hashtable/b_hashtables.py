

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.max = capacity
        self.count = 0
        self.storage = [None] * capacity
    
    def resize(self):
        ratio = self.count / self.max
        if(ratio >= 0.2 and ratio <= 0.7):
            return
        multiplier = 2 if ratio > 0.7 else 0.5
        self.max = round(self.max * multiplier)
        self.storage = [self.storage[i] if i < self.count else None for i in range(self.max)]


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    k = 33
    for char in string:
        hash = (hash * k) + ord(char)
    return hash % max - 1


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # Handle collions via linked list
    index = hash(key, hash_table.max)
    pair = hash_table.storage[index]
    if(pair != None):
        while(pair.next != None):
            pair = pair.next
        pair.next = Pair(key, value)
    else:
        hash_table.storage[index] = Pair(key, value)
    hash_table.count += 1
    hash_table.resize()


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.max)
    pair = hash_table.storage[index]

    if (pair == None):
        print(f"!!Warning!! There is no {key} in the table!")
    else:
        if(pair.key == key):
            hash_table.storage[index] = pair.next
        else:
            while(pair.next.key != key and pair.next != None):
                pair = pair.next
            if(pair.next == None):
                print(f"!!Warning!! There is no {key} in the table!")
                return
            pair.next = pair.next.next
        hash_table.count -= 1
        hash_table.resize()



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.max)
    return hash_table.storage[index]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "test", "Here today...\n")
    hash_table_insert(ht, "test1", "Here today...\n")
    hash_table_insert(ht, "line", "Here today...\n")

    if hash_table_retrieve(ht, "line") is None:
        print("ERROR, NOT FOUND!")
        return
        
    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE", hash_table_retrieve(ht, "line"))


Testing()
