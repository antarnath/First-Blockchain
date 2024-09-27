import sys
sys.path.append('/run/media/antarnath/Antar/Blockchain/Build_Blockchain')

from Blockchain.backend.core.block import Block
from Blockchain.backend.core.blockheader import BlockHeader
from Blockchain.backend.util.util import hash256, decode_base58
from Blockchain.backend.core.database.database import BlockchainDB
from Blockchain.backend.core.Tx import CoinbaseTx
from multiprocessing import Process, Manager
from Blockchain.frontend.run import main
import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
  def __init__(self, utxos):
    self.utxos = utxos
    
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
    
  def store_utxos_in_cache(self, Transaction):
    self.utxos[Transaction.TxId] = Transaction
    
  def addBlock(self, BlockHeight, prevBlockHash):
    timestamp = int(time.time())
    coinbaseInstance = CoinbaseTx(BlockHeight)
    coinbaseTx = coinbaseInstance.CoinbaseTransaction()
    merkleRoot = coinbaseTx.TxId
    bits = 'ffff001f'
    blockHeader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
    blockHeader.mine()
    self.store_utxos_in_cache(coinbaseTx)
    print(f'Block {BlockHeight} mined successfully with nonce {blockHeader.nonce}')
    self.write_on_disk([Block(BlockHeight, 1, blockHeader.__dict__, 1, coinbaseTx.to_dict()).__dict__])

  
  def main(self):
    lastBlock = self.fetch_last_block()
    if lastBlock is None:
      self.GenesisBlock()
    while True:
      lastBlock = self.fetch_last_block()
      BlockHeight = lastBlock['Height'] + 1   
      prevBlockHash = lastBlock['BlockHeader']['blockHash']
      self.addBlock(BlockHeight, prevBlockHash)
    
if __name__ == '__main__':
  with Manager() as manager:
    utxos = manager.dict()
    
    webapp = Process(target = main, args = (utxos,))
    webapp.start()
    
    blockchain = Blockchain(utxos)
    blockchain.main()

