import sys
inp = []
out = []
vowels = ["a", "e", "i", "o", "u"]
for line in sys.stdin:
    inp.append(line.strip().lower())


#consEndIndex = 0;
j = 0 #j is the current index
for word in inp:
    firstVowel = False
    consonants = ""
    i = 0
    #i is last consonant index, and will be used to slice string
    for char in word:
        if word[0] in vowels:
            inp[j] += "-yay"
            firstVowel = True
            break
        if char not in vowels:
            consonants+=char
            i += 1
        else:
            break
    if(firstVowel == False):
        consonants += "ay"
        inp[j] = word[i:] + "-" + consonants
    j+=1

for words in inp:
    print(words)
