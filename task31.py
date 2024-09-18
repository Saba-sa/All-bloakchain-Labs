
import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_tree(hashes):
    if len(hashes) % 2 == 1:
        hashes.append(hashes[-1])
    new_hashes = []
    for i in range(0, len(hashes), 2):
        new_hash = sha256(hashes[i] + hashes[i + 1])
        new_hashes.append(new_hash)
    if len(new_hashes) == 1:
        return new_hashes[0]
    else:
        return merkle_tree(new_hashes)

# Read file and divide it into 8 blocks
file_path = 'lecture_slides.txt'  # Update this with the actual file path
with open(file_path, 'r') as file:
    content = file.read()

block_size = len(content) // 8
blocks = [content[i*block_size:(i+1)*block_size] for i in range(8)]

# Calculate their hashes
hashes = [sha256(block) for block in blocks]

# Construct the Merkle tree and print the root hash
merkle_root = merkle_tree(hashes)
print(f"Merkle Root: {merkle_root}")

