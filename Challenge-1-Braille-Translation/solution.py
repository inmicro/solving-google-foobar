braille_map = {
	'a' : '100000',
	'b' : '110000',
	'c' : '100100',
	'd' : '100110',
	'e' : '100010',
	'f' : '110100',
	'g' : '110110',
	'h' : '110010',
	'i' : '010100',
	'j' : '010110',
	'k' : '101000',
	'l' : '111000',
	'm' : '101100',
	'n' : '101110',
	'o' : '101010',
	'p' : '111100',
	'q' : '111110',
	'r' : '111010',
	's' : '011100',
	't' : '011110',
	'u' : '101001',
	'v' : '111001',
	'w' : '010111',
	'x' : '101101',
	'y' : '101111',
	'z' : '101011',
}

capital_mark = '000001'
blank_mark = '000000'

def solution(s):
    # Your code here
	c = 1
	final_string = ''
	for word in s.split():
		for letter in word:
			l = letter.lower()
			if l in braille_map:
				if letter.isupper():
					final_string += capital_mark 
					final_string += braille_map[l]
				else:
					final_string += braille_map[letter]
		if len(s.split()) > 1 and c != len(s.split()):
			final_string += blank_mark
			c += 1


	return final_string

# TEST
print(solution('The quick brown fox jumps over the lazy dog') == '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110')