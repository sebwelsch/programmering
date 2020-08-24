import json
import requests

rates = requests.get('https://api.exchangeratesapi.io/latest')

print(rates.text)

rateOne = input('Hvilken valuta ønsker du at konvertere fra? ')
if rateOne in rates.keys():

    rateTwo = input('Hvilken valuta ønsker du at konvertere til? ')
    if rateTwo in rates.keys():
            amount = int(input('Beløb '))
            print('Omregnet ' + rateOne +  ' ' + str(amount) + ' til ' + rateTwo + ' ' + str(amount * rates[rateTwo]))
