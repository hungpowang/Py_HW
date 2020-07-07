import requests
from bs4 import BeautifulSoup as bs
import prettytable
import ssl
import warnings

# Issue handling
ssl._create_default_https_context = ssl._create_unverified_context  # SSL for MacOS
warnings.filterwarnings('ignore')  # remove warning from bs

url = "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html"
param = {"ID": "Tue%20Jul%2007%202020%2017:28:26%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)"}

response = requests.get(url, params=param).text
html = bs(response)

cities_name = html.find_all("th", scope="row")
cities_tmp = html.find_all("span", class_="tem-C is-active")

table = prettytable.PrettyTable(['地區', '氣溫'], encoding='utf8')
for (c, t) in zip(cities_name, cities_tmp):
    table.add_row([c.text, t.text])
print(table)
