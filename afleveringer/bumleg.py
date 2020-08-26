x = True

def tryAgain():
    print('Fejl, prøv igen')

def checkForBum(tal, bumtal):
    if tal % bumtal == 0:
        print('BUM!')
        return True
    elif str(bumtal) in str(tal):
        print('BUM!')
        return True
    else:
        print(str(tal))
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

            bumtal = int(input('Vælg et bumtal '))

            for tal in range(1, 1000):
                checkForBum(tal, bumtal)

        else:
            tryAgain()

    elif gamemodeOne == 'Nej':

        x = False

        print()
        print('Computeren spiller nu selv')

        bumtal = int(input('Vælg et bumtal '))

        for tal in range(1, 51):
            checkForBum(tal, bumtal)

    else:
        tryAgain()
