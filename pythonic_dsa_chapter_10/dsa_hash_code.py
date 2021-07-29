def hash_code(s):
    mask = (1 << 32) - 1    # limit to 32-bit integers
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    return h


print(hash_code("al"))