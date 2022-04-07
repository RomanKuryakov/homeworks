import datetime as dt
import requests
import json


url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)

d = json.loads(response.text)

date = dt.datetime.utcnow() + dt.timedelta(hours=3)
def currency_rates(cur):
  cur = cur.upper()
  curr_list = d['Valute']
  date = d['Date'].split('T')
  date = date[0]
  print ('курс на', date)
  if cur not in curr_list:
    return None
  else:
    for cost in curr_list:
      curr_name = curr_list[cur]
      cost = round(float(curr_name['Value']), 2)
      return cost


print(currency_rates(input('Введите название индекса: ')))
