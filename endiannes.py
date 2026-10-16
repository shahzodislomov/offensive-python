n = 0x12345678
def int_to_little_endian(n, length):
     return n.to_bytes(length, byteorder="little")
def int_to_big_endian(n, length):
     return n.to_bytes(length, byteorder="big")
print(int_to_little_endian(n, 4).hex())
print(int_to_big_endian(n, 4).hex())
