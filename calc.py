def additionCalc():
    print('A, S, M, or D?')
    temp = input()
    if temp != 'A' and temp != 'S' and temp != 'M' and temp != 'D':
        print('Error Run Again.')
    if temp == 'A':
        print('Input First Value:')
        fV = input()
        print('Input Second Value:')
        sV = input()
        sum = int(fV) + int(sV)
        print('Sum is: ' + str(sum))
    if temp == 'S':
        print('Input First Value:')
        fV = input()
        print('Input Second Value:')
        sV = input()
        sum = int(fV) - int(sV)
        print('Sum is: ' + str(sum))
    if temp == 'M':
        print('Input First Value:')
        fV = input()
        print('Input Second Value:')
        sV = input()
        sum = int(fV) * int(sV)
        print('Sum is: ' + str(sum))
    if temp == 'D':
        print('Input First Value:')
        fV = input()
        print('Input Second Value:')
        sV = input()
        sum = int(fV) / int(sV)
        print('Sum is: ' + str(sum))
    
additionCalc()

