people=["王琪","张苗青","张静静","杨苗","魏东"]
def list():
    for pe in people:
        print(pe)
def tjxs():
    tj = input("请添加一个学生:")
    people.append(tj)
    list()
def xgxs():
    xb = int(input("请输入修改学生学号："))
    mz = input("请输入所修改信息：")
    people[xb] = mz
    list()
def xhsc():
    xh = int(input("请输入删除学生学号"))
    del people[xh]
    list()

list()
gess=1
while gess:

    xuanxiang=["添加学生","修改学生信息","删除学生","退出"]
    print(xuanxiang)
    m=int(input("请输入你所要的选项（用1,2,3,4表示）："))
    if m==1:
        tjxs()
    if m==2:
        xgxs()
    if m==3:
        print("有三种删除方法请选择：")
        xuxu=["学号删除","末尾删除","姓名删除"]
        print(xuxu)
        n = int(input("请输入你所要的选项（用1,2,3表示）："))
        if n==1:
            xhsc()
        if n==2:
            people.pop()
            list()
        if n==3:
            sname=input("请输入你要删除的学生名字")
            people.remove(sname)
            list()
    if m==4:
        print("已退出学生管理系统")
        break