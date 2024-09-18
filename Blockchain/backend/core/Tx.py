from Blockchain.backend.core.Script import Script
from Blockchain.backend.util.util import int_to_little_endian, bytes_needed

ZERO_HASH = b'\0 * 32'
REWARD = 50

PRIVATE_KEY = '21504145648019153397736658542531956956518261337744923999335140775838241169153'
MINER_ADDRESS = '1knBWVq9rEunSd2Q5cTY44FUFck4WzXyS'

class CoinBaseTx:
  def __init__(self, BlockHeight):
    self.BlockHeightInLittleEndian = int_to_little_endian(BlockHeight, bytes_needed(BlockHeight))
  
  def CoinbaseTransaction(self):
    prev_tx = ZERO_HASH 
    prev_index = 0xffffffff 
    
    tx_ins = []
    tx_ins.append(TxIn(prev_tx, prev_index))
    
    tx_outs = []
    target_amount = REWARD * 100000000
    

class Tx:
  def __init__(self, version, tx_ins, tx_outs, locktime):
    self.version = version
    self.tx_ins = tx_ins
    self.tx_outs = tx_outs
    self.locktime = locktime
    
class TxIn:
  def __init__(self, prev_tx, prev_index, script_sig = None, sequence = 0xffffffff):
    self.prev_tx = prev_tx
    self.prev_index = prev_index
    if script_sig is None:
      self.script_sig = Script()
    else:
      self.script_sig = script_sig
    self.sequence = sequence
    
    
class TxOut:
  def __init__(self, amount, script_pubkey):
    self.amount = amount
    self.script_pubkey = script_pubkey
    