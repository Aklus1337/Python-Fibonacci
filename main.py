Fibonacci = []


maxNumber=0
maxNumber = input("Give me the maximum index: ")
maxNumber=int(maxNumber)

if(int(maxNumber) <= 0):
    print("Too small number.you wrote the number:"  + str(maxNumber))
    input(maxNumber)

def generateNumbers():
    Fibonacci.append(0)
    Fibonacci.append(1)
    for i in range(2, maxNumber): #starting number is 2 as 0 and 1 already got numbers
        Fibonacci.append(Fibonacci[i-1] +Fibonacci[i-2])

    printNumbers()

def printNumbers():
    print("Printing numbers!")
    print(Fibonacci)

    indexNumber()

def indexNumber():
    index = input("Which number would you like to see? ")
    index=int(index)
    if(index<=len(Fibonacci)):
        print(str(Fibonacci[index-1]))
    else:
        print("Wrong number!")
        indexNumber()
    index=int(index)


generateNumbers()