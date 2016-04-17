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
