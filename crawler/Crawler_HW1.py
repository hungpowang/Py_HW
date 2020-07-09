import requests
import codecs

url = "http://teaching.bo-yuan.net/test/requests/"

#res = requests.get(url)
#print(res.text)
#print("status_code:",res.status_code)
#print("headers:",res.headers)
#print("encoding:",res.encoding)
#print("text:",res.text)
#print("content:",res.content)
#print(res.text)
# ---> encoding: ISO-8859-1


#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> 缺少參數「action」。


#res = requests.get(url, params={ "action":"hahaha" })
#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> 需要DELETE的操作。

#res = requests.delete(url, params={ "action":"hahaha" })
#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> 缺少資料「id」。

#res = requests.delete(url, params={ "action":"hahaha" }, data={"id":"999"})
#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> 記得去PUT操作。

#res = requests.put(url, params={ "action":"hahaha" }, data={"id":"999"})
#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> 需要更新資料「name」。

#res = requests.put(url, params={ "action":"hahaha" }, data={"id":"999", "name":"John"})
#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> PUT完了，也要PATCH資料。

#res = requests.patch(url, params={ "action":"hahaha" }, data={"id":"999", "name":"John"})
#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> 需要PATCH的資料是「address」。

#res = requests.patch(url, params={ "action":"hahaha" }, data={"id":"999", "name":"John", "address":"Taipei"})
#with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
#	f.write(res.text)
# "ISO-8859-1.html" ---> 最後POST一筆資料吧。

res = requests.post(url, params={ "action":"hahaha" }, data={"id":"999", "name":"John", "address":"Taipei"})
with codecs.open("ISO-8859-1.html", "w", "ISO-8859-1") as f:
	f.write(res.text)
# "ISO-8859-1.html" ---> 哈哈，答對了，請把操作過程中的所有指令保留在程式碼中，將檔案繳交上來。

