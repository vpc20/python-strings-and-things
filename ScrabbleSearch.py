def scrabble_search(tiles):
    infile = open(r'C:\Users\vpc\share\english3.txt')
    for word in infile:
        tiles_list = list(tiles.lower())
        valid_word = True
        for ch in word.strip().lower():
            if ch in tiles_list:
                tiles_list.remove(ch)
            else:
                valid_word = False
        if valid_word:
            yield word.strip()
    infile.close()


for w in scrabble_search('rstlneg'):
    print(w)



