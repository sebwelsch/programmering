def checkForBum(number, bumtalList):
    for n in bumtalList:
        if number % n == 0:
            return True
        if str(n) in str(number):
            return True
    return False

x = True

while x:
    print('Bumleg')

    numberList = []
    bumtalList = []

    bumtalWhile = True

    while bumtalWhile:
        bumtal = input('Vælg så mange bumtal du vil, "Stop" for at stoppe ')
        if bumtal == 'Stop':
            bumtalWhile = False
        else:
            bumtalList.append(int(bumtal))

    print(bumtalList)

    for number in range(1, 51):
        if checkForBum(number, bumtalList) == True:
            number =  str('BUM!')
            numberList.append(number)
        else:
            numberList.append(number)

    playing = True
    t = 0

    while playing:
        guess = input('Spiller 1: ')
        if guess == str(numberList[t]):
            print('Rigtigt')
        else:
            print('Forkert! Spiller 2 vandt')
            break
        t = t + 1
        guessTwo = input('Spiller 2: ')
        if guessTwo == str(numberList[t]):
            print('Rigtigt')
        else:
            print('Forkert! Spiller 1 vandt')
            break
        t = t + 1

    playAgain = input('Vil du spille igen?(Ja/Nej) ')
    if playAgain == 'Ja':
        x = True
    else:
        break
