gamemodeOne = input('Vil du selv spille?(Ja/Nej) ')

if gamemodeOne == 'Ja':
    gamemodeTwo = input('Hvor mange personer?(1/2) ')

    if gamemodeTwo == '1':
        print(1)
    elif gamemodeTwo == '2':
        print(2)
    else:
        print('Fejl, prøv igen')

elif gamemodeOne == 'Nej':

    def checkForBum(tal, bumtal):
        if tal % bumtal == 0:
            print(str(tal) + ' True')
        elif str(bumtal) in str(tal):
            print(str(tal) + ' True')
        else:
            print(str(tal) + ' False')

    bumtal = int(input('Vælg et bumtal '))

    for tal in range(1, 51):
        checkForBum(tal, bumtal)

else:
    print('Fejl, prøv igen')
