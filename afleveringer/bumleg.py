def tryAgain():
    print('Fejl, prøv igen')

def checkForBum(number, bumtal):
    if number % bumtal == 0:
        return True
    elif str(bumtal) in str(number):
        return True
    else:
        return False

gamemodeOne = input('Vil du selv spille?(Ja/Nej) ')
if gamemodeOne == 'Ja':

    howManyBumtal = int(input('Hvor mange bumtal skal være i spillet? '))

    bumtal = int(input('Vælg et bumtal '))

    numberList = []

    for number in range(1, 51):
        if checkForBum(number, bumtal) == True:
            number =  str('BUM!')
            numberList.append(number)
        elif checkForBum(number, bumtal) == False:
            numberList.append(number)
        else:
            tryAgain()

elif gamemodeOne == 'Nej':

    x = False

    print()
    print('Computeren spiller nu selv')

    bumtal = int(input('Vælg et bumtal '))
    rangeNumber = int(input('Til og med hvilket tal skal computeren spille til? '))

    for number in range(1, rangeNumber + 1):
        if checkForBum(number, bumtal) == True:
            print('BUM!')
        elif checkForBum(number, bumtal) == False:
            print(str(number))
        else:
            tryAgain()

else:
    tryAgain()
