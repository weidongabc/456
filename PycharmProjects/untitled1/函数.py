def add(a,b):#形式参数
    return a+b
a=int(input("请输入第一个整数"))
b=int(input("请输入第二个整数"))
sum=add(a,b)    #实际参数，不能改变
print("两个数的和为:",sum)

#1.必须参数
def fn1(str):
    print(str)

fn1("str")

#2.关键字参数
def fn2(str):
    return
    print(str)

fn2(str="关键字参数")



#3.默认参数
def fn3(name,age):
    print("姓名为:",name)
    print("年龄为:",age)
fn3(name="张三")


#4.不定长参数
def fn4(*str):
    print(type(str))
    for i in str:
        print(i)
fn4("张三",'男',23)

def fn5(a,*str):
    for i in str:
        print(i)

fn5(12,23,34,56)