import json
import requests

rates = 'https://api.exchangeratesapi.io/latest'

currency = requests.get(rates)

print(currency.text)

fromCurrency = input('Hvilken valuta ønsker du at konvertere fra? ')
if fromCurrency in currency.text():

    baseCurrency = {'base':fromCurrency}

    baseRate = requests.get(rates, params=baseCurrency)

    toCurrency = input('Hvilken valuta ønsker du at konvertere til? ')
    if toCurrency in currency.text():
            amount = int(input('Beløb '))
            print('Omregnet ' + fromCurrency +  ' ' + str(amount) + ' til ' + toCurrency + ' ' + str(amount * fromCurrency[toCurrency]))
