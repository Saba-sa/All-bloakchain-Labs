import hashlib
# online hash:3194f08145c2c0822af5663e65dd35be59f73a121cff8b238c1b14467fdec048
online_hash=input("please enter online hash")

with open('./Lab 6-8-2024.pdf', "rb") as lab6:
    lab6_binary = lab6.read()

def comparison(a,b):
  if(a==b):
    print("equal")
  else:
    print("not equal")

def sha256Calculation(data):
  return hashlib.sha256(data).hexdigest()

manuallycalculated_hash=sha256Calculation(lab6_binary)
comparison(online_hash,manuallycalculated_hash)

# question 2
text_file="./demo.txt"

with open(text_file,"w") as f:
  f.write("This is a sample text")

with open(text_file,"rb") as f:
  fbinary=f.read()
  
sha256CalculationofTXT=sha256Calculation(fbinary)
print('sha256 of txt file',sha256CalculationofTXT)


# question3
file1="./message1.bin"
file2="./message2.bin"

with open(file1,"rb")as file1:
  file1_binary=file1.read()
  
with open(file2,"rb")as file2:
  file2_binary=file2.read()

file1md5=hashlib.md5(file1_binary).hexdigest()
print('file1 md5',file1md5)

file2md5=hashlib.md5(file1_binary).hexdigest()
print('file2 md5',file2md5)
  
file1sha256=sha256Calculation(file1_binary)
print('file1 sha256',file1sha256)

file2sha256=sha256Calculation(file2_binary)
print('file2 sha256',file2sha256)
  
resultofMD5=comparison(file1md5,file2md5)
resultofSha256=comparison(file1sha256,file2sha256)

