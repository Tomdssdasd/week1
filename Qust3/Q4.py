import random
str="qwertyuiopasdfghjklzxcvbnm"
str1=""
for i in range(1000):
    a=random.choice(str)
    str1+=a
set=set(str)

zd={}
for i in set:
    zd[i]=str1.count(i)
print(zd)
