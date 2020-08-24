def getInput():
    userinput = input('What is your name, user? ')
    if userinput == '':
        userinput = getInput()
    return userinput

def makeMessage(alias, enemy, greeting):
    return 'Greetings {}. {}. Good luck defeating {}!'.format(alias, greeting, enemy)

user = getInput()
message = 'No message set'

if user == 'Bruce Wayne':
    message = makeMessage('Batman', 'The Joker', 'You are the hero Gotham deserves, but not the one it needs right now')
elif user == 'Katniss Everdeen':
    message = makeMessage('Mockingjay', 'President Snow', 'May the odds be ever in your favour')
elif user == 'Peter Parker':
    message = makeMessage('Spiderman', 'Din mor', 'Fuck dig')
elif user == 'Bruce Banner':
    message = makeMessage('', '', '')
elif user == 'Tony Stark':
    message = makeMessage('', '', '')
elif user == 'Alan Scott':
    message = makeMessage('', '', '')
else:
    message = makeMessage('Programmer', 'The Compiler', 'You are the 5%')

print(message)
