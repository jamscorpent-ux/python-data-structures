class HashTable:
    def __init__(self):
        # Initialize collection as an empty dictionary
        self.collection = {}

    def hash(self, key):
        # Compute the sum of Unicode values of each character in the string
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_val = self.hash(key)
        # If the hash value doesn't exist, create an empty dictionary as a bucket
        if hash_val not in self.collection:
            self.collection[hash_val] = {}
        # Store the key-value pair in the nested dictionary
        self.collection[hash_val][key] = value

    def remove(self, key):
        hash_val = self.hash(key)
        # Check if the hash value and the specific key exist
        if hash_val in self.collection and key in self.collection[hash_val]:
            # Delete the specific key-value pair
            del self.collection[hash_val][key]
            
            # Optional: Remove the hash bucket if it's now empty
            if not self.collection[hash_val]:
                del self.collection[hash_val]

    def lookup(self, key):
        hash_val = self.hash(key)
        # Check if the hash bucket exists and the key is within it
        if hash_val in self.collection and key in self.collection[hash_val]:
            return self.collection[hash_val][key]
        # Return None if the key is not found
        return None