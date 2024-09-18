class Block:
  """
   Block is a storage container that stores transactions 
  """
  def __init__(self, Height, Blocksize, BlockHeader, TxCounts, TxS):
    self.Height = Height
    self.Blocksize = Blocksize
    self.BlockHeader = BlockHeader
    self.TxCounts = TxCounts
    self.TxS = TxS