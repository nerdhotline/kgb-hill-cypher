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