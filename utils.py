# -------------------------------------------------------------------------------------------------------			
# UTILITY FUNCTIONS

def cleanText(text: str):
  text = text.lower().strip()
  table = str.maketrans('', '', " ?!-.,;:\\")
  return text.translate(table)

def convert(x):
  def itoa(num):
    return chr(int(num) % 26 + 97)
  def atoi(char):
    return (ord(char) - 97) % 26
  
  if isinstance(x, str):
    return [atoi(char) for char in list(x)]
  return ''.join([itoa(num) for num in list(x)])

def tokenize(txt:str, ogTxtlen:int, blockNum:int):
  tokens = [txt[i:i+blockNum] for i in range(0, len(ogTxtlen), blockNum)]
  tokens = [string for string in tokens if string]
  diff = blockNum - tokens[-1]
  
  if (diff != 0):
    tokens[-1] += ('x' * diff)
    
  return tokens
  
