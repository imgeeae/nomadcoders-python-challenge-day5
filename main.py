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
      num = col.contents[7].get_text()
      if (num != ''):
        country_dict[country] = num
        print(f"# {num} {country}")
  return country_dict

def input_currency_code():
  try:
    code = int(input("#: "))
  except ValueError:
    print("That wasn’t a number")
    input_currency_code()
    
print("Hello! Please choose select a country by number:")
currency_codes = get_currency_codes()
input_currency_code()

