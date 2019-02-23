phone=input("请输入有效的手机号")
list=[151,153,186,139,135]
try:
    int(phone)
    if(len(phone)==11):
        head=phone[0:3]
        bool=False
        for i in list:
            if(int(head)==(i)):
                bool=True
                break
        if(bool):
            print("有效手机号")
        else:
            print("不是有效手机号")
    else:
        print("不是有效的手机号")
except ValueError:
    print("不是有效的手机号")