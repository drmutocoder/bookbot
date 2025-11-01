





def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):

    words = text.lower()
    counta = 0
    countb = 0
    countc = 0
    countd = 0
    counte = 0
    countf = 0
    countg = 0
    counth = 0
    counti = 0
    countj = 0
    countk = 0
    countl = 0
    countm = 0
    countn = 0
    counto = 0
    countp = 0
    countq = 0
    countr = 0
    counts = 0
    countt = 0
    countu = 0
    countv = 0
    countw = 0
    countx = 0
    county = 0
    countz = 0
    count_special = 0

    for i in words:
        if i == "a":
            counta += 1
        if i == "b":
            countb += 1
        if i == "c":
            countc += 1
        if i == "d":
            countd += 1
        if i == "e":
            counte += 1
        if i == "f":
            countf += 1
        if i == "g":
            countg += 1
        if i == "h":
            counth += 1
        if i == "i":
            counti += 1
        if i == "j":
            countj += 1
        if i == "k":
            countk += 1
        if i == "l":
            countl += 1
        if i == "m":
            countm += 1
        if i == "n":
            countn += 1
        if i == "o":
            counto += 1
        if i == "p":
            countp += 1
        if i == "q":
            countq += 1
        if i == "r":
            countr += 1
        if i == "s":
            counts += 1
        if i == "t":
            countt += 1
        if i == "u":
            countu += 1
        if i == "v":
            countv += 1
        if i == "w":
            countw += 1
        if i == "x":
            countx += 1
        if i == "y":
            county += 1
        if i == "z":
            countz += 1
        if i == "!":
            count_special += 1

    count_list = [counta, countb, countc, countd, counte, countf, countg, counth, counti, countj, countk, countl, countm, countn, counto, countp, countq, countr, counts, countt, countu, countv, countw, countx, county, countz]

    return count_list
