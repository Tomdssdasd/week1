import random
l=[]
u=[]
for i in range(50):
    num=random.randint(-10,10)
    if num>0:
        l.append(num)
    elif num<0:
        u.append(num)
print("正数",l)
print("负数",u)