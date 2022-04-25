import sys
inp = []
out = []
for line in sys.stdin:
    inp.append(line.strip())

# for i in range(len(inp)-2):
#     if inp[i] == inp[i+1]:
#         x = inp[i+1]
#         inp.remove(x)

#out = [i for n, i in enumerate(inp) if i not in inp[:n]]

#inp.sort()
#print("")
for word in inp:
    if word not in out:
        out.append(word)
#out.sort()
# print("")
for word in out:
    print(word)
