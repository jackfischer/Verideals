def remove_paren():
    brands_file = open("oldbrands.txt")
    new_file = open("brands.txt", "a")
    lines = brands_file.readlines()
    for line in lines:
        newline = line.lower()
        if "(" in line:
            newline = line[0:line.index("(")-1].lower()
        new_file.write(newline)

#remove_paren()
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
        textWords = text.split()
        for word in textWords:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words

count_words(tfios())

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

#calculations(tfios())

#calculations([
    #"hey ethan do you like cars", "yes my favorite is a ford", "cool. i saw this show on abc the other day", "that's good, did you see it at walmart", "no, i saw it at ford", "cool", "hey do you like ford", "ford is good yeah"
#])


def shortFreq():
    old = open("enFreq.txt")
    new = open("freq.txt", "a")
    freqs = old.readlines()
    for x in range(0, 50000):
        new.write(freqs[x])
