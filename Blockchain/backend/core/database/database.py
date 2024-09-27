# old code in commit number 8
    
import os
import json

class BaseDB:
  def __init__(self):
    self.basepath = 'data'
    self.filepath = '/'.join((self.basepath, self.filename))
  
  def read(self):
    if not os.path.exists(self.filepath):
      print(f'File {self.filepath} not available')
      return []
    
    with open(self.filepath, 'r') as file:
      raw = file.readline()  # Use read() instead of readline() to read the full file
    
    if raw.strip() == "":  # If file is empty or contains only whitespace
      print(f'File {self.filepath} is empty')
      return []
    
    try:
      data = json.loads(raw)
    except json.JSONDecodeError as e:
      print(f'Error decoding JSON: {e}')
      return []  # Return an empty list if JSON decoding fails
    
    return data

  def write(self, item):
    data = self.read()
    if data:
      data = data + item
    else:
      data = item
    with open(self.filepath, 'w+') as file:
        file.write(json.dumps(data))

class BlockchainDB(BaseDB):
  def __init__(self):
      self.filename = 'blockchain'
      super().__init__()
    
  def lastBlock(self):
    data = self.read()
    if data:
      return data[-1]
    else:
      print("No blocks found.")
      return None

class AccountDB(BaseDB):
  def __init__(self):
    self.filename = 'account'
    super().__init__()