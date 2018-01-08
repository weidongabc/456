s = [{"name": "魏东", "sex": "男", "age": 22, "语文": "89", "英语": "90"},
    {"name": "王琪", "sex": "男", "age": 23, "语文": "86", "英语": "78"},
    {"name": "张静静", "sex": "女", "age": 21, "语文": "88", "英语": "87"},
    {"name": "张苗青", "sex": "女", "age": 22, "语文": "98", "英语": "99"},
    {"name": "杨", "sex": "女", "age": 22, "语文": "89", "英语": "90"},]

def f1():  # 定义功能菜单
    print("请输入序号选择功能")
    print( "1.查看信息")
    print( "2.增加信息")
    print( "3.删除信息")
    print( "4.修改信息")
    print( "5.查找学生")
    print( "6.返回上一级")
    print( "7.退出学生系统")

def f2():#简单菜单
    print("1:查看  2:增加  3:删除  4:修改")
    print("5:查找  6:返回  7:退出  ")

def sex(sexInput):  # 检查性别
    if len(sexInput) == 1 and (sexInput.lower() == "m" or sexInput.lower() == "f"):
        return True
    else:
        return False


def age(ageInput):  # 检查年龄输入是否正确
    if len(ageInput) == 2 and ageInput.isdigit() == True:
        return True
    else:
        return False


def Chinese(Cinput):  # 检查语文成绩输入是否正确
    if len(Cinput) == 2 and Cinput.isdigit() == True:
        return True
    else:
        return False


def nameListFunction():  #显示单个学生姓名信息
    nameList = []
    for i in range(len(s)):
        if s[i]["name"] not in nameList:
            nameList.append(s[i]["name"])
    return nameList


def findNameLocation(studentname):  # 通过名字找到学生位置
    for j in range(len(s)):
        if s[j]["name"] == studentname:
            return j


def listFunction():  # 定义显示现有学生信息函数
    for i in range(len(s)):
        studentInfo = s[i]
        print("姓名：%s 性别：%s 年龄：%s 语文：%s英语：%s" % (
        studentInfo["name"], studentInfo["sex"], studentInfo["age"], studentInfo["语文"], studentInfo["英语"]))


def add():  # 定义增加学生函数

    while True:
        numInput =input("修改已经存在的学生信息1 \n 增加一个新的学生请输入2：")
        if numInput == "2":
            while True:
                nameNoExistAdd = input("请输入您要增加的名字：")
                nameList = nameListFunction()
                if nameNoExistAdd in nameList:
                    print("%s在学生管理系统中已经存在" % nameNoExistAdd)

                else:
                    newStudent = {}
                    newStudent["name"] = nameNoExistAdd
                    while True:
                        sexInput = input("请输入%s的性别 f:男 m:女：" % nameNoExistAdd)
                        if sex(sexInput) == True:
                            newStudent["sex"] = sexInput
                            break
                        else:
                            print("输入有误，请重新输入！")
                    while True:
                        ageInput = input("请输入%s2位数字年龄：" % nameNoExistAdd)
                        if age(ageInput) == True:
                            newStudent["age"] = ageInput
                            break
                        else:
                            print("输入有误，请重新输入！")
                    while True:
                        Cinput = input("请输%s2位表示的语文成绩：" % nameNoExistAdd)
                        if Chinese(Cinput) == True:
                            newStudent["studentID"] = Cinput
                            break
                        else:
                            print("输入有误，请重新输入！")
                    extraInput = input("请输入%s2位表示的英语成绩：" % nameNoExistAdd)
                    newStudent["英语"] = extraInput
                    s.append(newStudent)
                    print("%s已经添加到学生管理系统" % nameNoExistAdd)
                    print("")
                    print("姓名：%s 性别：%s 年龄：%s 语文：%s 英语：%s--" % (
                    newStudent["name"], newStudent["sex"], newStudent["age"], newStudent["studentID"],
                    newStudent["英语"]))
                    break
            break
        elif numInput == "1":
            while True:
                nameExistAdd = input("请输入您要修改英语成绩的学生的名字：")
                nameList = nameListFunction()
                if nameExistAdd in nameList:
                    extraExistAdd = input("请输入您要添加的英语成绩：")
                    j = findNameLocation(nameExistAdd)
                    s[j]["英语"] = extraExistAdd
                    print("已经添加")
                    print("姓名：%s 性别：%s 年龄：%s 语文：%s--英语：%s--" % (
                    s[j]["name"], s[j]["sex"], s[j]["age"], s[j]["studentID"],
                    s[j]["英语"]))
                    break
                else:
                    print("您输入的姓名不存在")
            break
        else:
            print("您输入的信息不正确")


def delFunction():  # 定义删除学生的函数
    while True:
        nameDel = input("请输入您要删除的名字：")
        studentNameList = nameListFunction()
        if nameDel in studentNameList:
            j = findNameLocation(nameDel)
            del s[j]
            print("%s已经从学生管理系统中删除" % nameDel)
            break
        else:
            print("您要删除的名字不存在！")


def modifiFunction():  # 定义修改学生的函数
    while True:
        nameModifi = input("请输入要修改的名字：")
        studentNameList = nameListFunction()
        if nameModifi in studentNameList:
            print("请选择要修改的内容")
            print("1：修改姓名")
            print("2：修改性别")
            print("3：修改年龄")
            print("4：修改语文成绩")
            print("5：修改英语成绩")

            while True:
                choiceInput = input("请输入：")
                if choiceInput == "1":
                    newNameInput = input("请输入新的姓名：")
                    j = findNameLocation(nameModifi)
                    s[j]["name"] = newNameInput
                    print("姓名已经更新")
                    break
                elif choiceInput == "2":
                    while True:
                        newSexInput = input("请输入新的性别--f:男 m:女")
                        if sex(newSexInput) == True:
                            j = findNameLocation(nameModifi)
                            s[j]["sex"] = newSexInput
                            print("性别已经更新")
                            print("")
                            break
                        else:
                            print("有误，请重新输入！")
                    break
                elif choiceInput == "3":
                    while True:
                        newAgeInput = input("请输入新的年龄：")
                        if age(newAgeInput) == True:
                            j = findNameLocation(nameModifi)
                            s[j]["age"] = newAgeInput
                            print("年龄已经更新")
                            break
                        else:
                            print("有误，请重新输入！")
                    break
                elif choiceInput == "4":
                    while True:
                        newChinese = input("请输入新的语文成绩：")
                        if Chinese(newChinese) == True:
                            j = findNameLocation(nameModifi)
                            s[j]["studentID"] = newChinese
                            print("成绩已经更新")
                            break
                        else:
                            print("有误，请重新输入！")
                    break
                elif choiceInput == "5":
                    newEnglish = input("请输入新的英语：")
                    j = findNameLocation(nameModifi)
                    s[j]["英语"] = newEnglish
                    print("已经更新")
                    break
                else:
                    print("输入有误，请重新输入！")
            break
        else:
            print("您输入的名字不存在！")


def searchFunction():  # 定义搜索学生的函数
    nameSearch = input("请输入要查找的名字：")
    print("")
    nameList = nameListFunction()
    if nameSearch in nameList:
        print("%s在学生管理系统中" % nameSearch)
        j = findNameLocation(nameSearch)
        print("姓名：%s  性别：%s  年龄：%s  语文：%s  英语：%s " % (s[j]["name"], s[j]["sex"], s[j]["age"], s[j]["studenID"],
        s[j]["英语"]))
    else:
        print("%s不在学生管理系统中" % nameSearch)
        # 默认学生信息系统内容


f1()
while True:  # 进入循环，根据序号选择操作
    userInput = input("请输入您要选择的功能序号：")

    if userInput == "1":  # 显示
        listFunction()
        f2()
        continue
    elif userInput == "2":  #增加
        add()
        listFunction()
        f2()
        continue
    elif userInput == "3":  # 删除
        delFunction()
        listFunction()
        f2()
        continue
    elif userInput == "4":  # 修改
        modifiFunction()
        listFunction()
        f2()
        continue
    elif userInput == "5":  # 查找
        searchFunction()
        listFunction()
        f2()
        continue
    elif userInput == "6":  # 返回
        f1()
        listFunction()
        continue
    elif userInput == "7":  # 退出
        break
    else:
        print("输入有误，请重新输入！")
