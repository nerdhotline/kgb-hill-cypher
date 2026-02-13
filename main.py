import numpy as np 
from utils import cleanText, tokenize
from MTX import transform

# ----------------------------------------------------------------------------------------------------------------
# HILL CYPHER FUNCTIONS

def hillEncode(text:str, blockNum: int, key):	
  tokens = tokenize(cleanText(text), len(text), blockNum)
  encodedTokens = [transform(token, key) for token in tokens]
  return ''.join(encodedTokens)


def hillDecode(text:str, blockNum: int, key):
  tokens = tokenize(text, len(text), blockNum)
  decodedTokens = [transform(token, key, False) for token in tokens]
  return ''.join(decodedTokens)

