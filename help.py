import operator
import numpy as np
from matplotlib import pyplot as plt
import string

def remove_paren():
    brands_file = open("oldbrands.txt")
    new_file = open("brands.txt", "a")
    lines = brands_file.readlines()
    for line in lines:
        newline = line.lower()
        if "(" in line:
            newline = line[0:line.index("(")-1].lower()
        new_file.write(newline)

def shortFreq():
    old = open("enFreq.txt")
    new = open("freq.txt", "a")
    freqs = old.readlines()
    for x in range(0, 50000):
        new.write(freqs[x])

def getEngFreq():
    freqF = open("freq.txt")
    freqlines = freqF.readlines()
    freqs = {}
    for line in freqlines:
        data = line.split()
        freqs[data[0]] = float(data[1])
    return freqs

def fun():
    brandsfile = open("brands.txt")
    brands = brandsfile.readlines()
    prac = "this is my text and I like Ford cars they're pretty good i also like to eat Skittles and talk on my Verizon phone ABC"
    for brand in brands:
        brand = brand[0:len(brand)-1]
        if brand in prac:
            print brand

def tfios():
    tfiosfile = open("hp2.txt")
    lines = tfiosfile.readlines()
    return lines

def count_words(texts):
    words = {}
    for text in texts:
        text = text.translate(string.maketrans("",""), string.punctuation)
        textWords = text.split()
        for word in textWords:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words

def do_freqs(words):
    total = 0
    for word in words:
        total += words[word]
    freqs = {}
    for word in words:
        freqs[word.lower()] = (words[word]/1.0)/(total)
    return freqs

def calc_freqs(words, eng_words):
    freqs = {}
    for word in words:
        word = word.lower()
        if word in eng_words:
            freqs[word] = float(words[word]) - float(eng_words[word])
    return freqs

def calculations(texts):
    brandsfile = open("brands.txt")
    brands = brandsfile.readlines()
    used = {}
    for brand in brands:
        brand = " " + brand[0:len(brand)-1]
        for text in texts:
            text = text.lower()
            if brand in (" " + text):
                if brand[1:] in used:
                    used[brand[1:]] += 1
                else:
                    used[brand[1:]] = 1
    print used

lines = tfios()
words = count_words(lines)
freqs = do_freqs(words)
litfreqs = calc_freqs(freqs, getEngFreq())
final = sorted(litfreqs.items(), key=operator.itemgetter(1))
#for tup in final:
    #print str(tup[0]) + " " + str(tup[1])

wordsOnly = []
numsOnly = []
r = 20
for i in range(len(final)-r,len(final)):
    w = final[i]
    wordsOnly.append(w[0])
    numsOnly.append(w[1])

fig = plt.plot()
w= .75
ind = np.arange(r)
plt.bar(ind, numsOnly, width=w)
plt.xticks(ind + w / 2, wordsOnly, rotation='vertical')
plt.show()
