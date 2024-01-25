"""
Roadmap: https://neetcode.io/roadmap
YouTube Tutorial: https://www.youtube.com/watch?v=i-h0CtKde6w

Hashing in Python is a process of converting input data (or a message) into a fixed-length
string of characters, which is typically a hexadecimal number.
Hash functions are commonly used in various applications, such as data integrity verification,
password storage, and data indexing.
Python provides several built-in modules for hashing.
"""

import hashlib

print(hashlib.algorithms_available)
h = hashlib.sha256(b"Hello World")


# print(h)
print(h.digest()) # b'\xa5\x91\xa6\xd4\x0b\xf4 @J\x01\x173\xcf\xb7\xb1\x90\xd6,e\xbf\x0b\xcd\xa3+W\xb2w\xd9\xad\x9f\x14n'
print(h.hexdigest()) # a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e


h = hashlib.new("SHA256") # Another way
password = "Test1234"
h.update(password.encode())
print(h.hexdigest()) # 07480fb9e85b9396af06f006cf1c95024af2531c65fb505cfbd0add1e2f31573