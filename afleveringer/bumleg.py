x = True

def tryAgain():
    print('Fejl, prøv igen')

def checkForBum(number, bumtal):
    if number % bumtal == 0:
        print('BUM!')
        return True
    elif str(bumtal) in str(number):
        print('BUM!')
        return True
    else:
        print(str(number))
        return False

while x:
    gamemodeOne = input('Vil du selv spille?(Ja/Nej) ')
    if gamemodeOne == 'Ja':

        gamemodeTwo = input('Hvor mange spillere?(1/2) ')
        if gamemodeTwo == '1':
            x = False
            print(1)
        elif gamemodeTwo == '2':
            x = False
            playerOne = True
            playerTwo = True

            howManyBumtal = int(input('Hvor mange bumtal skal være i spillet? '))

            bumtal = int(input('Vælg et bumtal '))

            for number in range(1, 51):
                checkForBum(number, bumtal)

            while playerOne:
                guess = input('Spiller 1: ')
                if guess != checkForBum(number, bumtal):
                    print('Forkert! Spiller 2 vandt')
                    break

        else:
            tryAgain()

    elif gamemodeOne == 'Nej':

        x = False

        print()
        print('Computeren spiller nu selv')

        bumtal = int(input('Vælg et bumtal '))
        rangeNumber = int(input('Til og med hvilket tal skal computeren spille til? '))

        for number in range(1, rangeNumber + 1):
            checkForBum(number, bumtal)

    else:
        tryAgain()
