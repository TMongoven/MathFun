def collatz(x):
    steps = 0
    while int(x) != 1:
        if x%2 == 0:
            x = x/2
        else:
            x = (3*x)+1
        steps += 1
    return steps

def cont():
    while True:
        cont = input("Continue? ")
        if cont in {"YES", "Y", "Yes", "y", "yes"}:
            print("\n")
            break
        elif cont in {"NO", "N", "No", "n", "no"}:
            exit()
        else:
            print("Must be a yes or no response.")

def divisorsum(x):
    divisors = []
    divsum = 0
    j = 0
    for i in range (1, x):
        if x%i == 0:
            divisors.append(i)
    while j < len(divisors):
        divsum = divsum + divisors[j]
        j += 1
    if divsum < x:
        divstring = "a deficient (sum of factors < " + str(x) + ")"
    elif divsum == x:
        divstring = "a perfect (sum of factors = " + str(x) + ")"
    elif divsum > x:
        divstring = "an abundant (sum of factors > " + str(x) + ")"
    return divstring

def evendetect(x):
    if x%2 == 0:
        return 1
    else:
        return 0

def factorial(x):
    inew = 1
    factstring = "It cannot be represented as a factorial"
    for i in range (1, 20):
        inew = i*inew
        if x == inew:
            factstring = str(x) + " can be represented as " + str(i) + "!"
    return factstring
    
def mersenne(x):
    x = x+1
    while evendetect(x):
        x = x/2
    if x != 1:
        return 0
    else:
        return 1

def picheck(x):
    import os
    import sys
    with open(os.path.join(sys.path[0], "pi.txt"), "r") as f:
        string = f.read()
    index = string.find(str(x))
    index -= 1
    count = string.count(str(x))
    return index, count

def powercheck(x):
    powerstring = "It can be represented as "
    for i in range (2, 1000):
        root = x**(1/i)
        if (root).is_integer:
            if round(root)**i == x and int(root) != 1:
                apowerstring = str(round(root)) + " to the power of " + str(i)
                if powerstring != "It can be represented as ":
                    powerstring += " or " + apowerstring
                else: 
                    powerstring += apowerstring
    if powerstring == "It can be represented as ":
        return "It cannot be represented as a single exponential" 
    return powerstring            

def primecounterceiling(x):
    from math import sqrt
    primelist = []
    for i in range (2, x):
        comp = 0
        if i != 2 and i%2 == 0:
            i = i+1
            continue
        for j in range(3, (int(sqrt(i))+1), 2):
            if i%j == 0:
                comp = 1
                break
        if comp == 0:
            primelist.append(i)
        i = i+1
    return primelist
    
def primecounternum(x):
    from math import sqrt
    i = 2
    primelist = []
    while x>len(primelist):
        comp = 0
        if i != 2 and i%2 == 0:
            i += 1
            continue
        for j in range(3, (int(sqrt(i))+1), 2):
            if i%j == 0:
                comp = 1
                break
        if comp == 0:
            primelist.append(i)
        i += 1
    return primelist

def primedetect(x):
    from math import sqrt
    if x == 1:
        return 0
    if x != 2 and x%2 == 0:
        return 0
    for i in range (3, int((sqrt(x))+1), 2):
        if x%i == 0:
            return 0
    return 1

def primedist(x):
    distbelow = 0
    distabove = 0
    primeabove = 0
    primebelow = 0
    for i in range (1, x):
        y = x - i
        if primedetect(y):
            distbelow = i
            primebelow = y
            break
    for i in range (1, 100000):
        z = x + i
        if primedetect(z):
            distabove = i
            primeabove = z
            break
    if primebelow == 0:
        primebelow = "non-existent"
    else:
        primebelow = str(distbelow) + " away: " + str(primebelow)
    primeabove = str(distabove) + " away: " + str(primeabove)
    return primebelow, primeabove

def primefactorization(x):
    from math import sqrt
    factorlist=[]
    if x == 0:
        return
    if x == 1:
        string = "1 * 1"
        return string, factorlist
    string = ""
    xpart = x
    if primedetect(x):
        string += str(xpart) + " * 1"
        return string, factorlist
    else:
        while xpart%2 == 0:
            factorlist.append(str(2))
            xpart = xpart/2
        for i in range (3, int((sqrt(xpart))+1), 2):
            while int(xpart)%i == 0:
                factorlist.append(str(i))
                xpart = xpart/i
        if int(xpart) != 1:
            factorlist.append(str(int(xpart)))
            factorstring = ' * '.join(factorlist)
            string += factorstring
        else:
            factorstring = ' * '.join(factorlist)
            string += factorstring
        return string, factorlist
