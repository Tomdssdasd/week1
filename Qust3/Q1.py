phone=input("请输入手机号")
list=[151,186,153,139,156,187]
try:
    int(phone)
    if(len(phone)==11):
        head=phone[:3]
        bool=False
        for i in list:
            if(int(head)==(i)):
                bool=True
                break
        if(bool):
            print("合格")
        else:
            print("不合格")
    else:
        print("不合格")

except ValueError:
    print("不合格")