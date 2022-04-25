
inp = list(input().split())
for words in inp:
    filtered = ''.join(filter(str.isalnum, words))
    words = filtered
    print(words)
