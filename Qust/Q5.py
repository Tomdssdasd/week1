s='The column above illustrates apparently the polularity of people doing exercise in a certain year from 2013 to 2018 Based upon the data we can see that python is wonderful python is wonderful Python'

list=s.split(" ")
set=set(list)

zd={}
for i in set:
    zd[i]=s.count(i)
print(zd)

li=sorted(zd.items(),key=lambda x:x[1])
li2=dict(li)
print(li2)