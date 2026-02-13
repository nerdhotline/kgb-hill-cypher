# KENNETH BLAKE
# MATH475
# HILL CYPHER ENCODING

import numpy as np 



# -------------------------------------------------------------------------------------------------------			
# UTILITY FUNCTIONS

def cleanText(text: str):
  text = text.lower().strip()
  table = str.maketrans('', '', " ?!-.,;:\\")
  return text.translate(table)

def convert(x):
  def itoa(num):
    return chr(int(num % 26) + 97)
  def atoi(char):
    return (ord(char) - 97) % 26
  
  if (isinstance(x, str)):
    return [atoi(char) for char in list(x)]
  return ''.join([itoa(num) for num in list(x)])

def tokenize(txt:str, ogTxtlen:int, blockNum:int):
  tokens = [txt[i:i+blockNum] for i in range(0, ogTxtlen, blockNum)]
  tokens = [string for string in tokens if string]
  diff = blockNum - len(tokens[-1])
  
  if (diff != 0):
    tokens[-1] += ('x' * diff)
    
  return tokens

# -------------------------------------------------------------------------------------------------------			
# MATRIX FUNCTIONS

# isInvertible --> Checks if matrix is both square and has a non-zero determinant
def isInvertible(mtx:np.matrix):
  isSquare = mtx.shape[0] == mtx.shape[1]
  isDetZero = np.isclose(np.linalg.det(mtx), 0)
  return isSquare and not isDetZero 

# invertMtx --> Calculates a^(-1) (mod 26) and multiplies by the adjoint matrix
def invertMtx(mtx:np.matrix):
  det = int(np.round(np.linalg.det(mtx))) 
  det_inv = pow(det, -1, 26) 
  adj = np.round(det * np.linalg.inv(mtx)).astype(int)
  
  return (det_inv * adj) % 26
  
def transform(text: str, mtx: np.matrix, isEncode:bool = True):
  if (isInvertible(mtx)):
    # if we are decoding, flip the matrix
    mtx = mtx if isEncode else invertMtx(mtx)
    vec = convert(text)
    product = mtx @ vec
    norm = (product % 26).flatten().tolist()[0]
    return convert(norm)

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

# ----------------------------------------------------------------------------------------------------------------
# Testing
def test(plainTxt:str, key:np.matrix):
  ciphTxt = hillEncode(plainTxt, 2, key)
  deciphTxt = hillDecode(ciphTxt, 2, key)
  plainAsciiCodes = convert(deciphTxt) 
  ciphAsciiCodes = convert(ciphTxt) 
  print(f"PLAINTEXT: {plainTxt}\nASCII CODES(PLAINTEXT): {plainAsciiCodes}\nASCII CODES(CIPHERTEXT):{ciphAsciiCodes}\nCIPHERTEXT: {ciphTxt}\nDECRYPTED CIPHERTEXT: {deciphTxt}\n\n")

test(' Hello world.', np.matrix([[1, 3], [1, 8]]))
test('I love math', np.matrix([[1, 3], [1, 8]]))
test('Beam ME Up ScOtTy', np.matrix([[1, 3], [1, 8]]))