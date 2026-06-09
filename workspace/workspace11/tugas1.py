import hashlib
text = "UTDI"
hash_object = hashlib.sha256(text.encode('utf-8'))
hex_dig = hash_object.hexdigest()
print(f"SHA-256 Hash: {hex_dig}")

text2 = "Fakultas Teknologi Informasi"
hash_object2 = hashlib.sha256(text2.encode('utf-8'))
hex_dig2 = hash_object2.hexdigest()
print(f"SHA-256 Hash: {hex_dig2}")
