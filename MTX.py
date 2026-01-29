import numpy as np
from utils import convert

# -------------------------------------------------------------------------------------------------------			
# MATRIX FUNCTIONS

# isInvertible --> Checks if matrix is both square and has a non-zero determinant
def isInvertible(mtx:np.matrix):
	isSquare = mtx.shape[0] == mtx.shape[1]
	isDetZero = np.isclose(np.linalg.det(mtx), 0)
	return isSquare and not isDetZero 

# invertMtx --> Calculates a^(-1) (mod 26) and multiplies by the adjoint matrix
def invertMtx(mtx:np.matrix):
	adj = np.linalg.det(mtx) * np.linalg.inv(mtx)
	inverse = pow(int(np.linalg.det(mtx)), -1, 26)
	adj = inverse * adj
	return adj % 26
	
def transform(text: str, mtx: np.matrix, isEncode:bool = True):
	if (isInvertible(mtx)):
		# if we are decoding, flip the matrix
		mtx = mtx if isEncode else invertMtx(mtx)
		vec = convert(text)
		product = mtx @ vec
		norm = product % 26
		return convert(norm)