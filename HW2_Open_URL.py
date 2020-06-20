import webbrowser
import sys

if len(sys.argv) == 1:
   url = input("請輸入網址！ ")
else:
   url = sys.argv[1]
if 'https://' not in url:
   if 'http://' not in url:
       url = 'https://'+url
       print("missing \'http\'. Make it up as:", url)
webbrowser.open_new(url)