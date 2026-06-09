import hashlib
import time

class CoreBlockchain:
    def __init__(self, idx, data, previous_hash):
        self.idx = idx
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.count_hash()

    def count_hash(self):
        block_contents = (
            str(self.idx) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_contents.encode()).hexdigest()