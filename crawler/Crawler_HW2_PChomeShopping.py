import requests
import json
from os import system
import prettytable
import ssl

# Issue handling for MacOS
ssl._create_default_https_context = ssl._create_unverified_context  # SSL

url_part1 = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q="
url_q = None
url_part2 = "&page="
url_page = "1"
url_part3 = "&sort=sale/dc"


def show_table():
    col_names = ['名稱', '價格']
    table = prettytable.PrettyTable(col_names, encoding='utf8')
    table.align['名稱'] = "l"
    table.align['價格'] = "l"
    for prod in response['prods']:
        table.add_row([prod['name'], prod['price']])
    print(table)


# 要查詢的商品
url_q = input("關鍵字: ")

# 組成網址
url = url_part1 + url_q + url_part2 + url_page + url_part3

# 取得JSON
response = requests.get(url).json()
# 總頁數
totalpages = response['totalPage']

show_table()

url_page = input("前往頁碼：")
while int(url_page) <= totalpages:
    # 組成網址
    url = url_part1 + url_q + url_part2 + url_page + url_part3
    # 取得JSON
    response = requests.get(url).json()
    # system('clear')  # for MacOS
    system('cls')
    show_table()
    url_page = input("前往頁碼：")
print("頁碼超過範圍！")
