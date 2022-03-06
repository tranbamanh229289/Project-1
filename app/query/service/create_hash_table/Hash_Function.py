HASH = 5381
# a simple hashing algorithm with acceptable collision rate
def _djb2x_hash(string):
    hash = HASH
    byte_array = string.encode('utf-8')

    for byte in byte_array:
        # the modulus keeps it 32-bit, python ints don't overflow
        hash = ((hash * 33) ^ byte) % 0x100000000

    return hash
