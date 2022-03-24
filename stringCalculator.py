# test function will check the different test cases of string number
def test():    
    #Empty string
    assert(add("")== 0)

    #one Number
    assert(add("4") == 4)
    assert(add("2") == 2)

    #Two Number
    assert(add("1,2") == 3)
    assert(add("4,5") == 9)

    #multiple numbers
    assert(add("1,2,3,4,5") == 15)
    assert(add("20,30,40,50") == 140)

    #new lines between numbers
    assert(add("1\n2,3") == 6)
    assert(add("1,4\n3") == 8)

    #different delimeter
    assert(add("//;\n1;2") == 3)
    assert(add("//*\n5*5") == 10)

    #String number with negative numbers
    assert(add("//*\n5*-5*-10*-8")== "Exception")
    assert(add("//*\n5*15*10*4") == 34)

    print("All Test cases Completed Successfully")

#Below function will the check whether string number having any negative numbers
def checkNegativeNumbers(stringNumbers):
    negatives = []
    isNegativeExist = False
    for number in stringNumbers:
        if int(number)< 0:
            negatives.append(int(number))
    if len(negatives) > 0:
        isNegativeExist = True
    return (negatives, isNegativeExist)

#Main function
def add(inputString):
    if len(inputString) == 0:
        return 0
    elif len(inputString) == 1 and inputString.isnumeric():
        return int(inputString)
    else:
        try:
            delimeter = ","
            inputString = inputString.replace("\n", ",")
            if inputString[0] == "/" and inputString[1] == "/":
                    delimeter = inputString[2]
                    inputString = inputString[4:]
            stringNumbers = inputString.split(delimeter)
            checkNegativeExist  = checkNegativeNumbers(stringNumbers)
            if checkNegativeExist[1]:
                raise Exception('negatives not allowed --> {}'.format(checkNegativeExist[0]))
            total = sum([int(num) for num in stringNumbers])
            return total    
        except Exception as e:
            print (e)
            return "Exception"

test()
