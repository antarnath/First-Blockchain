import sys
sys.path.append('/run/media/antarnath/Antar/Blockchain/Build_Blockchain')

from Blockchain.backend.core.block import Block
from Blockchain.backend.core.blockheader import BlockHeader
from Blockchain.backend.util.util import hash256
from Blockchain.backend.core.database.database import BlockchainDB
import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
  def __init__(self):
    self.GenesisBlock()
    
  def write_on_disk(self, block):
    blockchainDB = BlockchainDB()
    blockchainDB.write(block)
    
  def fetch_last_block(self):
    blockchainDB = BlockchainDB()
    return blockchainDB.lastBlock()
    
  def GenesisBlock(self):
    BlockHeight = 0
    prevBlockHash = ZERO_HASH
    self.addBlock(BlockHeight, prevBlockHash)
    
  def addBlock(self, BlockHeight, prevBlockHash):
    timestamp = int(time.time())
    Transaction = f'Codies Alert Sent {BlockHeight} Bitcoin to Antar'
    merkleRoot = hash256(Transaction.encode()).hex()
    bits = 'ffff001f'
    blockHeader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
    blockHeader.mine()
    self.write_on_disk([Block(BlockHeight, 1, blockHeader.__dict__, 1, Transaction).__dict__])
    
  
  def main(self):
    while True:
      lastBlock = self.fetch_last_block()
      BlockHeight = lastBlock['Height'] + 1   
      prevBlockHash = lastBlock['BlockHeader']['blockHash']
      self.addBlock(BlockHeight, prevBlockHash)
    
if __name__ == '__main__':
  blockchain = Blockchain()
  blockchain.main()