### making a big index
def make_big_index(size):
	index = []
	letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
	while len(index) < size:
		word = make_string(letters)
		add_to_index(index, word, 'fake')
		for i in range(len(letters) - 1, 0, -1): 
			if letters[i] < 'z':
				letters[i] = chr(ord(letters[i])+ 1)
				break
		else:
			letters[i] = 'a'
	return index

def make_string(p):
	s = ""
	for e in p:
		s = s + e # add it to string s
	return s

def add_to_index(index, keyword, url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return 
	index.append([keyword,[url]])

#print make_big_index(3)
print make_big_index(10)