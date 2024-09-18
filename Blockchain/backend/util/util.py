import hashlib
from Crypto.Hash import RIPEMD160
from hashlib import sha256
from math import log
from Blockchain.backend.core.EllepticCurve.EllepticCurve import BASE58_ALPHABET
# BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def hash256(s):
  return hashlib.sha256(hashlib.sha256(s).digest()).digest()

def hash160(s):
  return RIPEMD160.new(sha256(s).digest()).digest()

def bytes_needed(n):
  if n == 0:
    return 1
  return int(log(n, 256)) + 1

def int_to_little_endian(n, length):
  """int_to_little_endian takes an integer and returns the little-endian byte"""
  return n.to_bytes(length, 'little')


def decode_base58(s):
  num = 0
  
  for c in s:
    num *= 58
    num += BASE58_ALPHABET.index(c)
    
  combined = num.to_bytes(25, byteorder='big')
  checksum = combined[-4:]
  
  if hash256(combined[:-4])[:4] != checksum:
    raise ValueError(f'Bad Address {checksum} {hash256(combined[:-4][:4])}')

  print(combined[1:-4])
  return combined[1:-4]

