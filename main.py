import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

def get_currency_codes():
  url = "https://www.iban.com/currency-codes"
  result = requests.get(url).text
  soup = BeautifulSoup(result, 'html.parser')
  country_table = soup.find("table").find_all("tbody")

  country_dict = {}
  for row in country_table:
    for col in row.find_all("tr"):
      country = col.contents[1].get_text()
      code = col.contents[5].get_text()
      num = col.contents[7].get_text()
      if (num != ''):
        print(f"# {int(num)} {country}")
        country_dict[int(num)] = [country.capitalize(), code]
  return country_dict

def find_currency_code(currency_codes):
  try:
    num = int(input("#:"))
    if num not in currency_codes:
      print("Choose a number from the list.")
      find_currency_code(currency_codes)
    else:
      print(f"You chose {currency_codes[num][0]}")
      print(f"The currency code is {currency_codes[num][1]}")

  except ValueError:
    print("That wasn’t a number")
    find_currency_code(currency_codes)


print("Hello! Please choose select a country by number:")
currency_codes = get_currency_codes()
find_currency_code(currency_codes)
