import unittest
from HashTable import HashTable # Pastikan nama fail anda hash_table.py

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_add_and_lookup(self):
        self.ht.add('golf', 'sport')
        self.assertEqual(self.ht.lookup('golf'), 'sport')

    def test_collision(self):
        # fcc dan cfc menghasilkan hash yang sama (300)
        self.ht.add('fcc', 'coding')
        self.ht.add('cfc', 'chemical')
        self.assertEqual(self.ht.lookup('fcc'), 'coding')
        self.assertEqual(self.ht.lookup('cfc'), 'chemical')

    def test_remove(self):
        self.ht.add('golf', 'sport')
        self.ht.remove('golf')
        self.assertIsNone(self.ht.lookup('golf'))

if __name__ == '__main__':
    unittest.main()
