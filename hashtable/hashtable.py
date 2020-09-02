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
        self.capacity = capacity
        # Create empty hash table with all None values
        self.hash_table = [None for i in range(capacity)]
        # Keeping track of the total number of keys for ll calculation
        self.total_keys = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hash_table) # also self.capacity should be fine


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # per Google: The load factor is the number of keys stored in the hash table divided by the capacity.
        return (self.total_keys / self.capacity)


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
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) + byte)

        return hash & 0xffffffff


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

        # Find the index
        index = self.hash_index(key)
        # Create variable for the value at index
        current_node = self.hash_table[index]

        # While the node has a value and we haven't reached the end of our list:
        while current_node is not None:
            # If the current node's key is key is the key we're looking for:
            if current_node.key == key:
                # Assign the value to the node
                current_node.value = value
                return
            else:
                # Or move on to the next node
                current_node = current_node.next

        # Create a new node with the HashTableEntry
        new_node = HashTableEntry(key, value)
        # Assign the index at the hash table we're on to be the .next node of the new_node
        new_node.next = self.hash_table[index]
        # Assign the new_node to the index we're on
        self.hash_table[index] = new_node

        # Add 1 to the total number of keys we're storing.
        self.total_keys += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # Find the index
        index = self.hash_index(key)
        # Set the value of the node of that index to None
        self.hash_table[index] = None

        # Reduce the total number of keys by 1
        self.total_keys -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Find the index
        index = self.hash_index(key)
        # Find the node at the index
        current_node = self.hash_table[index]

        # If node is not empty:
        while current_node is not None:
            # And the current node's key is the key we're looking for:
            if current_node.key == key:
                # Return the value of the key
                return current_node.value 
            else:
                # Or move on to check the next node
                current_node = current_node.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        # new_capacity = self.capacity * 2
        old_table = self.hash_table
        new_table = [None for i in range(new_capacity)]
        self.hash_table = new_table
        self.capacity = new_capacity

        for i in range(len(old_table)):
            current_node = old_table[i]
            while current_node is not None:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next





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

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
