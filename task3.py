import hashlib

def calculate_sha256(data):
    """Calculate the SHA-256 hash of the given data."""
    return hashlib.sha256(data).hexdigest()

def parse_file(file_path, num_blocks):
    """Parse the file into a specified number of blocks."""
    blocks = []
    with open(file_path, 'rb') as file:
        while True:
            block = file.read(len(file.read()) // num_blocks)
            if not block:
                break
            blocks.append(block)
    return blocks[:num_blocks]

def create_merkle_tree(hashes):
    """Create a Merkle tree and calculate the Merkle root."""
    if not hashes:
        return None

    while len(hashes) > 1:
        new_hashes = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i + 1] if i + 1 < len(hashes) else hashes[i]
            combined = left + right
            new_hashes.append(calculate_sha256(combined.encode('utf-8')))
        hashes = new_hashes

    return hashes[0]

def main(file_path, num_blocks):
    # Parse the file into blocks
    blocks = parse_file(file_path, num_blocks)
    
    # Calculate the SHA-256 hash for each block
    hashes = [calculate_sha256(block) for block in blocks]
    
    # Create the Merkle tree and print the Merkle root
    merkle_root = create_merkle_tree(hashes)
    print(f"Merkle Root: {merkle_root}")

# Replace 'path_to_your_file.txt' with the path to your file
file_path = 'path_to_your_file.txt'
num_blocks = 8

if __name__ == '__main__':
    main(file_path, num_blocks)
