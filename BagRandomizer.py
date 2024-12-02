from random import randint
def random7bag():
    finalbag = []
    bag = ['S','Z','L','J','I','T','O']
    for i in range(7):
        x = randint(0,len(bag) - 1)
        finalbag.append(bag[x])
        del bag[x]
    return finalbag
