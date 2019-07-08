

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.max = capacity
        self.count = 0
        self.hash_table = [None] * capacity
        


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    k = 33
    for char in string:
        newHash = (hash * k) + ord(char) % max - 1
    return hash


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.max)
    if(hash_table[index] !== None):
        print(f"!!Warning!!  You have overridden {hash_table[index]} with {value}!")
        hash_table.count -= 1
    hash_table[index] = Pair(key, value)
    hash_table.count += 1


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash_table.hash(key, hash_table.max)

    if (hash_table[index] == None):
        print(f"!!Warning!! There is no {key} in the table!")
    else:
        hash_table[index] == None
        hash_table.count -= 1



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.max)
    return hash_table[index]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
