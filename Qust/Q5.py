
s="The column above illustrates apparently the polularity of people doing exercise in a certain year from 2013 to 2018 Based upon the data we can see that python is wonderful python is wonderful Python"
result={}
for i in  set(s):
    result[i]=s.count(i)
print(result)
for k in sorted(result,key=result.__getitem__):
    print(k,result[k])