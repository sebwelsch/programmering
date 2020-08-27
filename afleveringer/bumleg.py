x = True

def tryAgain():
    print('Fejl, prøv igen')

def checkForBum(number, bumtal):
    if number % bumtal == 0:
        return True
    elif str(bumtal) in str(number):
        return True
    else:
        return False

while x:
    gamemodeOne = input('Vil du selv spille?(Ja/Nej) ')
    if gamemodeOne == 'Ja':

            x = False
            playerOne = True
            playerTwo = False

            howManyBumtal = int(input('Hvor mange bumtal skal være i spillet? '))

            bumtal = int(input('Vælg et bumtal '))

            for number in range(1, 51):
                checkForBum(number, bumtal)

            while playerOne:
                guess = input('Spiller 1: ')
                if guess != checkForBum(number, bumtal):
                    print('Forkert! Spiller 2 vandt')
                    break

            while playerTwo:
                guess = input('Spiller 2: ')
                if guess != checkForBum(number, bumtal):
                    print('Forkert! Spiller 1 vandt')
                    break

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
