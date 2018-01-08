#def fn(*str):
   # print(max(str))
#fn(123,234,742)

def dg(s):
    if s>=1:
        jc=s*dg(s-1)
    else:
        jc=1
        return jc
    n=("请输入一个整数")
    jc=dg(s)
    print(s)


