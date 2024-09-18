import os
import binascii
import base58
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def generate_pub_private_key:
  private_key = ec.generate_private_key(ec.SECP256R1())
  public_key = private_key.public_key()
  return private_key, public_key

private_key, public_key =generate_pub_private_key()

def bitcoin_walletAddress(pub_key):
  return hashlib.sha256(pub_key).hexdigest()

walletAddress=bitcoin_walletAddress(public_key)
  

