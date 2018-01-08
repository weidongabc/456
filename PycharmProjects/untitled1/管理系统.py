stu={'魏东':{'姓名':'魏东','年龄':22,'语文':89,'数学':99,'英语':90}}



def f1():
    print("添加")
    vname=input("请输入学生的姓名:")
    vage = int(input("请输入学生的年龄:"))
    vdata= input("请输入学生的成绩:")

    #stu={"name":vname,"age":vage,"data":vdata}#字典

def f2():
    print("查找")
    name=input("请输入要查找姓名：")
    count=0
    for stu in stus:
        if stu["name"]==name:
            print("学生已找到！")
            print("%s\t%d\t%s"%(stu["name"],stu["age"],stu["data"]))
            break
        count+=1
        if count==len(stus):
            print("该学生不存在")


def f3():
        print("修改")
        name=input("请输入要修改姓名：")
        count=0
        for stu in stus:
            if stu["name"]==name:
                print("学生已经找到！")
                print("%s\t%d\t%s"%(stu["name"],stu["age"],stu["data"]))
                break
            count+=1
        if count==len(stus):
            print("该学生不存在")
        else:
            stus[count]["name"]=input("请输入学生的姓名:")
            stus[count]["age"] = int(input("请输入学生的年龄:"))
            stus[count]["data"]= input("请输入学生的成绩:")
            print("修改已完成！")
            print("%s\t%d\t%s"%(stus[count]["name"],stus[count]["age"],stus[count]["data"]))


def f4():
    print("删除")
    name=input("请输入要查找姓名")
    count=0
    for stu in stus:
        if stu["name"] == name:
            print("学生已找到：")
            print("%s\t%d\t%s"%(stu["name"],stu["age"],stu["data"]))
            del stus[count]
            print("学生已删除")
            break
        count+=1
    if count == len(stus):
        print("学生不存在")

def f5():
    print("查看")
    print("姓名\n年龄\n学号")
    for stu in stus:
        print("%s\t%d\t%s"%(stu["name"],stu["age"],stu["data"]))#当名字很长时，表格混乱




print("="*30)
print("学生管理系统".center(24)) #汉字与“=”长度不等
print("输入1：添加")
print("输入2：查找")
print("输入3：修改")
print("输入4：删除")
print("输入5：查看")
print("输入6：退出")

stus=[]  #用来存储所有学生的列表

#处理用户输入

while True:
    op=input("请输入你的操作：")

    if op=="1":
        f1()

    elif op=="2":
        f2()

    elif op=="3":
        f3()

    elif op=="4":
       f4()

    elif op=="5":
        f5()

    elif op=="6":
        break
