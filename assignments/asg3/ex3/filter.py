import sys
inp = list(input().split())
#inp = []
for words in inp:
    filtered = ''.join(filter(str.isalnum, words))
    print(filtered)
