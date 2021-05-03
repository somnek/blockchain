## hashes: output is always predictable for the same input
import hashlib
# Hash functions expect bytes as input: the encode() method turns string into bytes
input_bytes = b'backpack'
output = hashlib.sha256(input_bytes)

# convert to hex (easier to read)
hexed = output.hexdigest()

print(f"output = {output}")
print(f"hexed = {hexed}")


