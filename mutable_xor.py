def xor_bytes(data: bytearray, key: int):
    for i in range(len(data)):
        data[i] ^= key
data = bytearray(b"Hello World!")
key = 0x42
print("Original data:", data)
xor_bytes(data,key)
print("XORed data:", data)
xor_bytes(data,key)
print("Restored data:", data)
