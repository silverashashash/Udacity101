def add_to_index(index,keyword,url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return index
	index.append([keyword,[url]])