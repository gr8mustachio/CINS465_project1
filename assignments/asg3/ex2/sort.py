import sys
inp = []
for line in sys.stdin:
    inp.append(line)
inp.sort()
for words in inp:
    print(words, end="")
