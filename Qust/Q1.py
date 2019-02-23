phone=input("请输入手机号")
str=[151,169,186,153,139,187]
try:
    int(phone)
    if(len(phone)==11):
        head=phone[0:3]
        bool=False
        for i in str:
            if (int(head)==i):
                bool=True
                break
        if(bool):
            print("符合")
        else:
            print("不符合")
    else:
        print("不是有效的")
except ValueError:
    print("不会有效的")
