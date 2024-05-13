import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode())
        return sha.hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, new_data, latest_block.hash)
        self.chain.append(new_block)

# Let's use it.
blockchain = Blockchain()
blockchain.add_block("Item 1")
blockchain.add_block("Item 2")

for block in blockchain.chain:
    print(f"Block {block.index}: {block.data}")