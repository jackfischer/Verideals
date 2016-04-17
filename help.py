import operator
import numpy as np
import en
from matplotlib import pyplot as plt
import string
import ebay
import json

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
    tfiosfile = open("tfios.txt")
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

def brand_calcs(texts):
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
    return used

def remove_extras(freqs):
    verblines = open("verbs.txt").readlines()
    for verbb in verblines:
        verbb = verbb[:len(verbb)-1]
        if verbb in freqs:
            del freqs[verbb]
        try:
            pastt = en.verb.past(verbb)
            #print pastt
            if pastt in freqs:
                del freqs[pastt]
        except:
            pass
    adjlines = open("adjs.txt").readlines()
    for adj in adjlines:
        adj = adj[:len(adj)-1]
        if adj in freqs:
            del freqs[adj]
    otherlines = open("thingList.txt").readlines()
    for other in otherlines:
        other = other[:len(other)-1]
        if other in freqs:
            del freqs[other]
    namelines = open("names.txt").readlines()
    for nameish in namelines:
        name = nameish.split(',')[0].lower()
        if name in freqs:
            del freqs[name]
    for word in freqs.keys():
        try:
            plur = en.noun.plural(word)
            if plur != word and plur in freqs:
                freqs[word] = freqs[word] + freqs[plur]
                del freqs[plur]
        except:
            print "oh boy"
    return freqs

def getFreqy(lines=tfios()):
    words = count_words(lines)
    freqs = do_freqs(words)
    litfreqs = calc_freqs(freqs, getEngFreq())
    litfreqs = remove_extras(litfreqs)
    final = sorted(litfreqs.items(), key=operator.itemgetter(1))

    wordsOnly = []
    numsOnly = []
    r = 20 #num columns
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

def getBrands(words=count_words(tfios())):
    brands = brand_calcs(words)
    r = -1
    if len(brands) > 20:
        r = 20
    else:
        r =len(brands)
    brands = sorted(brands.items(), key=operator.itemgetter(1))
    brandNames = []
    brandFreqs = []
    for i in range(len(brands) - r,len(brands)):
        try:
            brandNames.append(str(brands[i][0]))
            brandFreqs.append(brands[i][1])
        except:
            print brands[i][0]

    fig = plt.plot()
    w = .75
    ind = np.arange(r)
    plt.bar(ind, brandFreqs, width=w)
    plt.xticks(ind + w / 2, brandNames, rotation='vertical')
    plt.show()




def ebaydeals():
    textfile = open("texts.txt")
    texts = textfile.readlines()
    #getFreqy(texts)
    #getBrands(words=count_words(texts))
    brands = brand_calcs(texts)
    brands = sorted(brands.items(), key=operator.itemgetter(1))
    ebaydeals = {}
    for x in range(len(brands)-5 ,len(brands)):
        jsonebay = ebay.deals(brands[x][0])
        '''
        for item in jsonebay['searchResult']['item']:
            print item
            print ""
        '''
        dict = {}
        dict['title'] = jsonebay['searchResult']['item'][0]['title']
        dict['url'] jsonebay['searchResult']['item'][0]['viewItemURL']
        dict['price'] = jsonebay['searchResult']['item'][0]['sellingStatus']['convertedCurrentPrice']['value']
        dict['image_url'] = jsonebay['searchResult']['item'][0]['galleryURL']
        ebaydeals.append(dict)
    return ebaydeals
