import json

currency = {'DKK':1, 'EUR':7.5, 'USD':1, 'AUD':1, 'GBP':1, 'SEK':1, 'NOK':1}

currencyOne = input('Hvilken valuta ønsker du at konvertere fra? ')
if currencyOne in currency.keys():

    currencyTwo = input('Hvilken valuta ønsker du at konvertere til? ')
    if currencyTwo in currency.keys():
            amount = int(input('Beløb '))
            print('Omregnet ' + currencyOne +  ' ' + str(amount) + ' til ' + currencyTwo + ' ' + str(amount * currency[currencyTwo]))
