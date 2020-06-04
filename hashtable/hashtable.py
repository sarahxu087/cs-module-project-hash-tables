class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.array = [None]* self.capacity
        self.size = 0
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity
        
    

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        hash_entry=HashTableEntry(key,value)
        cur = self.array[slot]
        last = None
        while cur is not None and cur.key != key:
            last = cur
            cur = last.next

        if cur is not None:
            cur.value = value
        else:
            new = hash_entry
            new.next = self.array[slot]
            self.array[slot] = new
            self.size += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        cur = self.array[slot]
        last = None

        while cur is not None and cur.key != key:
            last = cur
            cur = last.next
        if cur is None:
            print("ERROR: Unable to remove key " + key)
        else:
            if last is None:  
                self.array[slot] = cur.next
            else:
                last.next = cur.next
            self.size-=1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        cur = self.array[slot]
        while cur is not None:
            if(cur.key == key):
                return cur.value
            cur = cur.next
        return None 



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        new = HashTable(new_capacity)
        cur = None
        for i in range(len(self.array)):
            cur = self.array[i]
            while cur is not None:
                new.put(cur.key,cur.value)
                cur = cur.next

        return new
        

'''
if __name__ == "__main__":
 ht = HashTable(8)

ht.put("line_1", "'Twas brillig, and the slithy toves")
ht.put("line_2", "Did gyre and gimble in the wabe:")
ht.put("line_3", "All mimsy were the borogoves,")
ht.put("line_4", "And the mome raths outgrabe.")
ht.put("line_5", '"Beware the Jabberwock, my son!')
ht.put("line_6", "The jaws that bite, the claws that catch!")
ht.put("line_7", "Beware the Jubjub bird, and shun")
ht.put("line_8", 'The frumious Bandersnatch!"')
ht.put("line_9", "He took his vorpal sword in hand;")
ht.put("line_10", "Long time the manxome foe he sought--")
ht.put("line_11", "So rested he by the Tumtum tree")
ht.put("line_12", "And stood awhile in thought.")
ht.get("line_12")
print("")

    # Test storing beyond capacity
    #for i in range(1, 13):
        #print(ht.get(f"line_{i}"))


  # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
'''