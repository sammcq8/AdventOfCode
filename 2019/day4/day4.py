def suffering():
    counter = 0
    for number in range(165432,707912):
        strNum = str(number)
        i = 0
        double = False
        lstNum = [char for char in strNum]

        digits = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 0:0}


        if sorted(lstNum) != lstNum:
            continue
        
        for dig in lstNum:
            digits[int(dig)] += 1
        for dig in digits:
            if digits[int(dig)] == 2:
                counter += 1
                break



            
                
    print(counter)


def check(sad_number):
    strNum = str(sad_number)
    i = 0
    double = False
    doubleSize = 0
    lstNum = [char for char in strNum]
    while i < 6:
        number = lstNum[i]
        nextNumber = number
        doubleSize = 0
        if number == nextNumber and i < 5:
            while number  == nextNumber and i < 5:
                doubleSize += 1
                nextNumber = lstNum[i+1]
                i += 1
            if doubleSize == 2:
                return True
        else:
            i += 1
    return False
    
    
        


def tryAgain():
    counter = 0
    for number in range(165432, 707912):
        number = str(number)
        doubles = 0
        doubleBool = False
        inc = True
        for i in range(6): 
           
            if i == 0:
                continue
            elif int(number[i]) == int(number[i-1]):
                doubles += 1
            elif int(number[i]) != int(number[i-1]) and doubles == 1:
                doubleBool = True
            if int(number[i]) < int(number[i-1]):
                inc = False
                break
            if doubleBool and inc:
                counter +=1
    print(counter)


print(check(111221))
suffering()