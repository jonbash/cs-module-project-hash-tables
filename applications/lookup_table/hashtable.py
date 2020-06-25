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
        self.__current_count = 0
        self.__buckets = [None] * capacity
        self.__fnv_offset_basis = 14695981039346656037
        self.__fnv_prime = 1099511628211

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.__current_count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hsh = self.__fnv_offset_basis
        key_bytes = [ord(char) for char in key]
        for byte in key_bytes:
            hsh *= self.__fnv_prime
            hsh ^= byte
        return hsh

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load_factor() > 0.7:  # resize if getting too big
            self.resize(self.capacity * 2)

        new_entry = HashTableEntry(key, value)
        idx = self.hash_index(key)
        bucket = self.__buckets[idx]

        if bucket is None or bucket.key == key:  # totally new or replacing
            self.__buckets[idx] = new_entry
        else:  # collision!
            while bucket.next is not None:
                bucket = bucket.next
            bucket.next = new_entry

        self.__current_count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        entry = self.__buckets[idx]

        if entry is not None and entry.key == key:  # found entry
            self.__buckets[idx] = entry.next
            print(f"deleting top-level '{key}'")
        else:
            while entry.next is not None and entry.next.key != key:
                entry = entry.next
            if entry.next is not None and entry.next.key == key:
                print(f"deleting nested '{key}'")
                entry.next = None
            else:
                print("Cannot remove; no value for key")
                return

        self.__current_count -= 1
        if self.get_load_factor() < 0.2 and self.capacity >= MIN_CAPACITY:
            # resize if getting too small
            self.resize(max(self.capacity // 2, MIN_CAPACITY))

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        entry = self.__entry_for_key(key)
        if entry is None:
            return None
        return entry.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        if self.capacity == new_capacity:
            return
        print(f"resizing from {self.capacity} to {new_capacity}")
        entries = []
        for entry in self.__buckets:
            if entry is not None:
                entries.append(entry)
                while entry.next is not None:
                    entries.append(entry.next)
                    entry = entry.next
        self.capacity = new_capacity
        self.__current_count = 0

        self.__buckets = [None] * self.capacity
        for entry in entries:
            self.put(entry.key, entry.value)

    def __entry_for_key(self, key):
        idx = self.hash_index(key)
        entry = self.__buckets[idx]
        while entry is not None:
            if entry.key == key:
                return entry
            entry = entry.next
        return entry


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
