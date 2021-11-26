import json
from datetime import date
import requests
import apiKey

# apiKey.ACCESS_KEY holds the ACCESS_KEY
with open('date.txt') as file:
    value = file.read()
if value != str(date.today()):
    with requests.get('http://api.exchangeratesapi.io/v1/latest?access_key={}'.format(apiKey.ACCESS_KEY)) as response:
        data = json.loads(response.text)
        with open('currency_value.json', 'w') as file:
            file.seek(0)
            json.dump(data, file, indent=2)
    with open('date.txt', 'w') as f:
        f.seek(0)
        f.write(str(date.today()))

price = float(input('Enter the price '))
country = input("enter the country: ").capitalize()
convertCurrency_country = input('Enter the country you want to change the value in: ').capitalize()

# get the country currency code now
with open('country_details.json') as file:
    data = json.load(file)
    currency_country = dict()
    for value in data['countries']['country']:
        currency_country[value['countryName']] = value['currencyCode']
    with open('currency_value.json') as test:
        data = json.load(test)
        all_rates = data['rates']
        try:
            if country in currency_country:
                country = currency_country[country]
            else:
                raise Exception('Base Country not found')
            if convertCurrency_country in currency_country:
                convertCurrency_country = currency_country[convertCurrency_country]
            else:
                raise Exception('No such country exist')
        except Exception as e:
            print(e)
        else:
            try:
                country_value = all_rates[country]
                currencyConvert_value = all_rates[convertCurrency_country]
            except KeyError:
                print('Country code mismatch')
            else:
                result = (currencyConvert_value/country_value) * price
                result = round(result, 2)
                print(f'{price} {country} in {convertCurrency_country} is {result}')
