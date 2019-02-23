import random
list=[]
for i in range(20):
    num=random.randint(0,10)
    list.append((num))
print(list)
list[::2]=sorted(list[::2])
list[::2].reverse()
print(list)