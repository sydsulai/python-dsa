def get_occurences(word, q):
    hash_dict = dict()
    for c in word:
        hash_dict[c] = hash_dict.get(c, 0)+1
    
    for i in q:
        print(hash_dict.get(i,0))

if __name__ == "__main__":
    word = "azyxyyzaaaa"
    q = ["d", "a", "y", "x"]
    get_occurences(word, q)