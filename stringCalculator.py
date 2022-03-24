# test function will check the different test cases of string number
def test():    
    #Empty string
    assert(add("")== 0)

    #one Number
    assert(add("4") == 4)
    assert(add("2") == 2)

    print("All Test cases Completed Successfully")

#Main function
def add(inputString):
    if len(inputString) == 0:
        return 0
    elif len(inputString) == 1 and inputString.isnumeric():
        return int(inputString)

test()
