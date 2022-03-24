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

    print("All Test cases Completed Successfully")

#Main function
def add(inputString):
    if len(inputString) == 0:
        return 0
    elif len(inputString) == 1 and inputString.isnumeric():
        return int(inputString)
    else:
        delimeter = ","
        inputString = inputString.replace("\n", ",")
        stringNumbers = inputString.split(delimeter)
        total = sum([int(num) for num in stringNumbers])
        return total    

test()
