[![Docker Build & Test](https://github.com/jamscorpent-ux/python-data-structures/actions/workflows/python-app.yml/badge.svg)](https://github.com/jamscorpent-ux/python-data-structures/actions/workflows/python-app.yml)
# Hash Table Implementation (Python)

A custom implementation of a **Hash Table** data structure built from scratch in Python. This implementation handles key-value pairs and manages potential hash collisions using a chaining approach (nested dictionaries).

## Features
- **Hash Function:** Converts string keys to integer hash values based on Unicode (ASCII) sum.
- **Collision Handling:** Uses nested dictionaries to store multiple key-value pairs that share the same hash index.
- **Methods:**
  - `add(key, value)`: Adds or updates a key-value pair.
  - `remove(key)`: Deletes a specific key-value pair without clearing the entire hash bucket.
  - `lookup(key)`: Retrieves the value associated with a key.

## Usage
```python
ht = HashTable()
ht.add('golf', 'sport')
ht.lookup('golf') # Returns 'sport'
