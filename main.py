import numpy as np 
from utils import cleanText
from MTX import transform

# ----------------------------------------------------------------------------------------------------------------
# HILL CYPHER FUNCTIONS

def hillEncode(text:str, blockNum: int, key):	
	cleaned, tokens, encodedTokens = '', [], []

	# Clean text, tokenized based on blockNum
	cleaned = cleanText(text)
	tokens = [cleaned[i:i+blockNum] for i in range(0, len(text), blockNum)]
	tokens = [string for string in tokens if string]
	lastTokenDiff = blockNum - tokens[-1] 

	# Normalize last token, make its length match all other tokens
	if (lastTokenDiff != 0):
		tokens[-1] += ('x' * lastTokenDiff)
	
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

