def tryAgain():
    print('Fejl, prøv igen')

def checkForBum(number, bumtal):
    if number % bumtal == 0:
        return True
    elif str(bumtal) in str(number):
        return True
    else:
        return False

x = True

while x:
    gamemodeOne = input('Vil du selv spille?(Ja/Nej) ')
    if gamemodeOne == 'Ja':

        bumtal = int(input('Vælg et bumtal '))

        numberList = []

        for number in range(1, 51):
            if checkForBum(number, bumtal) == True:
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
                x = False
                break
            t = t + 1
            guessTwo = input('Spiller 2: ')
            if guessTwo == str(numberList[t]):
                print('Rigtigt')
            else:
                print('Forkert! Spiller 1 vandt')
                break
            t = t + 1

    elif gamemodeOne == 'Nej':

        x = False

        print()
        print('Computeren spiller nu selv')

        rangeNumber = int(input('Til og med hvilket tal skal computeren spille til? '))
        bumtal = int(input('Vælg et bumtal '))

        for number in range(1, rangeNumber + 1):
            if checkForBum(number, bumtal) == True:
                print('BUM!')
            elif checkForBum(number, bumtal) == False:
                print(str(number))
            else:
                tryAgain()

    else:
        tryAgain()

    playAgain = input('Vil du spille igen?(Ja/Nej) ')
    if playAgain == 'Ja':
        x = True
    else:
        break
