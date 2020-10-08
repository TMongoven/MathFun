# Could probably be streamlined to not have so damn many print statements
# Takes in a number and returns many fun facts about that number

from NumberFunctions import *
from sys import exit


while True:
    try:
        x = int(input("Give me a number: "))
        polarity = ("odd", "even")[evendetect(x)]
        composition = ("composite", "prime")[primedetect(x)]
        mersness = (" is not", " is")[mersenne(x)]
        index, count = picheck(x)
        factorization, factorlist = primefactorization(x)
        if len(factorlist) == 2:
            composition += " (semiprime, meaning there are only two factors for this number aside from 1 and itself)"
        print("Fun facts about " + str(x) + ":")
        print("It is " + polarity + " and " + composition)
        print("It is " + divisorsum(x) + " number")
        print("The nearest prime below " + str(x) + " is " + primedist(x)[0])
        print("The nearest prime above " + str(x) + " is " + primedist(x)[1])
        print("The prime factorization of " + str(x) + " is " + factorization)
        print("There are " + str(len(primecounterceiling(x))) + " primes below " + str(x))
        print("Prime #" + str(x) + " is " + str(primecounternum(x)[-1]))
        print(powercheck(x))
        print("It takes %s steps for %s to reach one through the Collatz Conjecture" % (collatz(x), x))
        print("It" + mersness + " a Mersenne number (2^n-1)")
        print(factorial(x))
        print("This number shows up for the first time at decimal place #" + str(index) + " of pi")
        print(str(x) + " shows up " + str(count) + " times in the first 100,000 digits of pi")
        cont()
    except ValueError:
        print("That isn't a number, silly. Try again, but this time with an actual number.")
        print("\n")
        continue    