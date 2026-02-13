import numpy as np 
from utils import cleanText, tokenize
from MTX import transform

# ----------------------------------------------------------------------------------------------------------------
# HILL CYPHER FUNCTIONS

def hillEncode(text:str, blockNum: int, key):	
  cleaned, tokens, encodedTokens = '', [], []

  # Clean text, tokenized based on blockNum
  cleaned = cleanText(text)
  tokens = tokenize(cleaned, len(text), blockNum)
  
  # Add an entire block of filler characters (optional)
  # tokens.append('x' * blockNum)

  encodedTokens = [transform(token, key) for token in tokens]
  return ''.join(encodedTokens)


def hillDecode(text:str, blockNum: int, key):
  tokens, decodedTokens = [], []
  tokens = [text[i:i+blockNum] for i in range(0, len(text), blockNum)]
  tokens = [string for string in tokens if string]
  
  decodedTokens = [transform(token, key, False) for token in tokens]
  return ''.join(decodedTokens)

