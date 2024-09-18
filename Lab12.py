from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

message='I\'m using RSA'
def generate_rsa():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypting_message(message, public_key):
    ciperText = public_key.encrypt(
        message.encode('utf-8'),
        padding.PKCS1v15()
    )
    return ciperText

def decrypt_message(CipherText, private_key):
    plaintext = private_key.decrypt(
        CipherText,
        padding.PKCS1v15()
    )
    return plaintext.decode('utf-8')


private_key, public_key = generate_rsa()
encrypted_message = encrypting_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, private_key)

print('RSA Public Key:',public_key)
print('RSA Private Key:',private_key)
print('Plaintext:',message)
print('Ciphertext:',encrypted_message)
print('Decrypted Text:',decrypted_message)



#DAS
message="I'm using RSA"
from cryptography.hazmat.primitives.asymmetric import dsa
def  generateDSAKeyPair():
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()
    return private_key,private_key

def DSASign(privateKey, message):
    sign = private_key.sign(
    message.encode(),
    hashes.SHA256()
    )
    return sign
def DSAVerify(publicKey, message, signature):
    try:
       public_key.verify(
        signature,
        message.encode(),
        hashes.SHA256()
        )
       return True
    except Exception:
        return False

private_key,public_key=generateDSAKeyPair()
signature=DSASign(private_key,message)
signature_verification=DSAVerify(public_key,message,signature)

    
print(" DSA details") 
print("DSA Public Key:",public_key)
print("DSA Private Key:",private_key)
print("Message:",message)
print("Signature:",signature)
print("Verification:",signature_verification)
 
    
    
    # 
    
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def generateECDSKeyPair():
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key()
    return private_key, public_key

def ECDSASign(private_key, message):
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA3_256())
    )
    return signature

def ECDSVerify(public_key, message, signature):
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False

def main():
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSKeyPair()
    message = b'Message for ECDSA algorithm'
    signature = ECDSASign(ECDSAPrivateKey, message)
    verification = ECDSVerify(ECDSAPublicKey, message, signature)
    print("ECDSA:")
    print(ECDSAPublicKey)
    print(ECDSAPrivateKey)
    print(message.decode())
    print(signature)
    print(verification)

main()
