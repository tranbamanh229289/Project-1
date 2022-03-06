# from app.query.service.create_hash_table.Hash_Function import _djb2x_hash
from .Hash_Function import _djb2x_hash
import json

N_HASH_TABLE = 60000

with open("D:/20211/Project I/Project-1-Reverse-Index-Search/data/list_dict.json") as f1:
    list_dict = json.load(f1)

with open("D:/20211/Project I/Project-1-Reverse-Index-Search/data/list_doc_id.json") as f2:
    list_doc_id = json.load(f2)

class _Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __str__(self):
        return "'{}': '{}'".format(self.key, self.value)

class HashTable(object):
    def __init__(self, capacity):
        self.bucket_array = [None for i in range(capacity)]
        self.capacity = capacity

    def insert(self, key, value):
        key_hash = _djb2x_hash(key)
        bucket_index = key_hash % self.capacity

        new_node = _Node(key, value)
        existing_node = self.bucket_array[bucket_index]

        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    # found existing key, replace value
                    existing_node.value = value
                    return
                last_node = existing_node
                existing_node = existing_node.next_node
            # if we get this far, we didn't find an existing key
            # so just append the new node to the end of the bucket
            last_node.next_node = new_node
        else:
            self.bucket_array[bucket_index] = new_node

    def lookup(self, key):
        key_hash = _djb2x_hash(key)
        bucket_index = key_hash % self.capacity

        existing_node = self.bucket_array[bucket_index]
        if existing_node:
            while existing_node:
                if existing_node.key == key:
                    return list_doc_id[existing_node.value]
                existing_node = existing_node.next_node
            #if existing_node == None:
              #print(f'Your search - "{key}"- did not match any documents.')
        return None

    def delete(self, key):
        key_hash = _djb2x_hash(key)
        bucket_index = key_hash % self.capacity

        existing_node = self.bucket_array[bucket_index]
        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    if last_node:
                        last_node.next_node = existing_node.next_node
                    else:
                        self.bucket_array[bucket_index] = existing_node.next_node
                last_node = existing_node
                existing_node = existing_node.next_node

    def debug_print(self):
        for i in range(self.capacity):
            node = self.bucket_array[i]
            print('Bucket {}'.format(i))
            if node:
                while node:
                    print('    {}'.format(node))
                    node = node.next_node
            else:
                print('    Empty')

def insertHashTable(hashTable):
    for item in list_dict:
        hashTable.insert(item[0], item[2])
    return hashTable

hash_table = insertHashTable(HashTable(N_HASH_TABLE))
print(hash_table.lookup('D'))
