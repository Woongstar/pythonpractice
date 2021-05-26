# 초보자를 위한 파이썬 300제
#41~50

ticker = "btc_krw"
a = ticker.upper()
print(a)

ticker = "BTC_KRW"
b = ticker.lower()
print(b)

a = "hello"
a=a.capitalize()
print(a)

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

a = "hello world"
b=a.split()[0]
c=a.split()[1]
print(b)
print(c)

d=ticker.split("_")[0]
e=ticker.split("_")[1]
print(d,e)

date = "2020-05-01"
date.split("-")

data = "039490     "
data.rsplit()