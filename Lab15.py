import hashlib
import random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def generateTxid():
    return hashlib.sha256(str(random.randint(1, 1000000)).encode()).hexdigest()

def generateInput():
    prevTxid = generateTxid()
    prevOutputIndex = random.randint(0, 5)
    return prevTxid, prevOutputIndex

def generateOutput():
    recipientAddress = 'recipient_address' + str(random.randint(0, 100))
    amount = round(random.uniform(0.001, 1.0), 8)
    return recipientAddress, amount

def generateTransactionFee():
    return round(random.uniform(0.0001, 0.001), 8)

def generateRandomTransaction():
    txid = generateTxid()
    inputPrevTxid, inputPrevOutputIndex = generateInput()
    outputRecipientAddress, outputAmount = generateOutput()
    transactionFee = generateTransactionFee()
    return txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee                                          

def concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee):
    transactionData = str(txid) + str(inputPrevTxid) + str(inputPrevOutputIndex) + str(outputRecipientAddress) + str(outputAmount) + str(transactionFee)
    return transactionData

def generateECDSAKeyPair():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey = ECDSAPrivateKey.public_key()
    return ECDSAPrivateKey, ECDSAPublicKey

def ECDSASign(privateKey, message):
    message_bytes = message.encode() if isinstance(message, str) else message
    signature = privateKey.sign(message_bytes, ec.ECDSA(hashes.SHA256()))
    return signature

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(signature, message.encode(), ec.ECDSA(hashes.SHA256()))  # Ensure message is in bytes
        return True
    except Exception as e:
        return False
  
def main():
    txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()
  
    transactionDataAsMessage = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee)
  
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage.encode()).hexdigest()
  
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
  
    signature = ECDSASign(ECDSAPrivateKey, transactionDataAsMessageSHA256Hashed)
  
    verified = ECDSAVerify(ECDSAPublicKey, transactionDataAsMessageSHA256Hashed, signature)
    print("ECDSA:")
    print("ECDSA Public Key:", ECDSAPublicKey)
    print("ECDSA Private Key:", ECDSAPrivateKey)
    print("transactionDataAsMessageSHA256Hashed:", transactionDataAsMessageSHA256Hashed)
    print("Signature:", signature)
    print("Verification:", verified)

main()
