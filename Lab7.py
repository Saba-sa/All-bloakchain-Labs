import hashlib;

data1="And now the end is here And so I face that final curtain My friend I'll make it clear I'll state my case, of which I'm certain I've lived a life that's full I traveled each and every highway And more, much more I did it, I did it my way"

data2="Regrets, I've had a few But then again too few to mention I did what I had to do I saw it through without exemption I planned each charted course Each careful step along the byway And more, much, much more I did it, I did it my way"

data3="Yes, there were times I'm sure you knew When I bit off more than I could chew But through it all, when there was doubt I ate it up and spit it out I faced it all and I stood tall and did it my way"

data4=" For what is a man, what has he got? If not himself then he has naught Not to say the things that he truly feels And not the words of someone who kneels Let the record shows I took all the blows and did it my way"


def calculateSHa256(data):
    return hashlib.sha256(data.encode()).hexdigest()


def addTwoHashes(data1, data2):
  return data1 + data2


hash1=calculateSHa256(data1)
print('hash1:',hash1)
hash2=calculateSHa256(data2)
print('hash2:',hash2)
additionOfHash1n2=addTwoHashes(hash1,hash2)
print('addition1 and 2:',additionOfHash1n2)

hash3=calculateSHa256(data3)
print('hash3:',hash3)
hash4=calculateSHa256(data4)
print('hash4:',hash4)
additionOfHash3n4=addTwoHashes(hash3,hash4)
print('addition3 and 4:',additionOfHash3n4)


uphash1=calculateSHa256(additionOfHash1n2)
print("upper1:",uphash1)
uphash2=calculateSHa256(additionOfHash3n4)
print("upper2:",uphash2)
additionoflast=addTwoHashes(uphash1,uphash2)
print("lastoneadditon:",additionoflast)


roothash=calculateSHa256(additionoflast)

print(roothash)
# task2
randomStrings=['task1', 'task2','task3','task4','task5','task6','task7','task8']

hash1=calculateSHa256(randomStrings[0])
hash2=calculateSHa256(randomStrings[1])
additionOfHash1n2=addTwoHashes(hash1,hash2)
print('addition1 and 2:',additionOfHash1n2)

hash2=calculateSHa256(randomStrings[2])
hash3=calculateSHa256(randomStrings[3])
additionOfHash3n4=addTwoHashes(hash2,hash3)
print('addition3 and 4:',additionOfHash3n4)

hash4=calculateSHa256(randomStrings[4])
hash5=calculateSHa256(randomStrings[5])
additionOfHash5n6=addTwoHashes(hash3,hash4)
print('addition3 and 4:',additionOfHash5n6)


hash6=calculateSHa256(randomStrings[6])
hash7=calculateSHa256(randomStrings[7])
additionOfHash6n7=addTwoHashes(hash6,hash7)
print('addition7 and 8:',additionOfHash6n7)


hashaddition1n2=calculateSHa256(additionOfHash1n2)
hashaddition3n4=calculateSHa256(additionOfHash3n4)
hashaddition5n6=calculateSHa256(additionOfHash5n6)
hashaddition7n8=calculateSHa256(additionOfHash6n7)


hashaddition12n34=addTwoHashes(hashaddition1n2,additionOfHash3n4)
hashaddition56n78=addTwoHashes(hashaddition5n6,hashaddition7n8)
addhashesof12345678=addTwoHashes(hashaddition12n34,hashaddition56n78)



roothash=calculateSHa256(addhashesof12345678)

print('root hash:',roothash)

# task3 
import hashlib


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

def file_in_block(filename, num_blocks=8):
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
