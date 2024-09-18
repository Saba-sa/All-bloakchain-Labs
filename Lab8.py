import hashlib

def calculateSHa256(data):
    return hashlib.sha256(data.encode()).hexdigest()


def addTwoHashes(data1, data2):
  return data1 + data2

def readfilesinBlocks(hashes):
    while len(hashes) > 1:
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])
        
        new_hashes = []
        for i in range(0, len(hashes), 2):
            combine_hashes = calculateSHa256(hashes[i] + hashes[i+1])
            new_hashes.append(combine_hashes)
        
        hashes = new_hashes
    return hashes[0]

def file_in_block(filename, num_blocks=1024):
    with open(filename, "rb") as file:
        content = file.read()
    
    block_size = len(content) // num_blocks
    blocks = [content[i:i + block_size] for i in range(0, len(content), block_size)]
    return blocks

def blocks_to_hashes(blocks):
    return [calculateSHa256(block.hex()) for block in blocks]

filename = './Lab 7-8-2024.pdf'
blocks = file_in_block(filename)
hashes = blocks_to_hashes(blocks)
root = readfilesinBlocks(hashes)

print(root)