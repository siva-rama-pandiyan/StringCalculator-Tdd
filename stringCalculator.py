# test function will check the different test cases of string number
def test():    
    #Empty string
    assert(add("")== 0)
    print("All Test cases Completed Successfully")
    
#Main function
def add(inputString):
    if len(inputString) == 0:
        return 0
test()
