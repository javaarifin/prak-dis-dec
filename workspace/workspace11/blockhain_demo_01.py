import UtdiBlockchain

informatika_blockchain = UtdiBlockchain.UtdiBlockchain()
informatika_blockchain.add_block("Bambang transfer ke Zaky sebesar 5 koin")
informatika_blockchain.add_block("Zaky transfer ke Didik sebesar 10 koin")

for block in informatika_blockchain.chain:
    print(f"Blok #{block.idx}")
    print(f"Data: {block.data}")
    print(f"Hash Sebelumnya: {block.previous_hash}")
    print(f"Hash Sekarang : {block.hash}\n" + "-"*40)