# 초보자를 위한 파이썬 300제
#31~40

a="3"
b="4"
print(a+b)

print("hi"*3)

print("-"*80)

t1="python"
t2="java"
print((t1+' '+t2+' ')*3)

name1="김민수"
age1=10
name2="이철희"
age2="13"

print("이름:{} 나이:{}".format(name1,age1))
print("이름:{} 나이:{}".format(name2,age2))


print(f"이름 {name1} 나이 {age1}")

상장주식수="5,969,782,550"
제거 = 상장주식수.replace(",","")
print(제거)

분기 = "2020/03(E) (IFRS연결)"
제거1 = 분기[:7]
print(제거1)

data = "   삼성전자    "
data1 = data.strip()
print(data1)