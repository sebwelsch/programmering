def checkForBum(tal, bumtal):
    if tal % bumtal == 0:
        print(str(tal) + ' True')
    elif str(bumtal) in str(tal):
        print(str(tal) + ' True')
    else:
        print(str(tal) + ' False')

bumtal = 3

for tal in range(1, 51):
    checkForBum(tal, bumtal)
