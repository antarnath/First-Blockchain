def GenesisBlock(self):
    BlockHeight = 0
    prevBlockHash = ZERO_HASH
    self.addBlock(BlockHeight, prevBlockHash)