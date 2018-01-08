#列表的定义
#name=[]

#列表的遍历，列表的循环输出
#for i in range(9):
#    print(i)

#for snmae in name:
#    print(snmae)

#字符串是否可以改变
#s="abdc"
#s[2]='c'
#print(s)


#列表的内置函数
#1.append()
name=["张三","李四"]
name.append("王五")
for nam in name:
    print(nam)


#信息，姓名，年龄，性别
people=["张三",18,"男"]
people[1]=20
for po in people:
    print(po)

sname=input("请输入您要查找的学生")
if sname in people:
    print("已到")
else:
    print("缺勤")


names=["张三","李四","王五","赵六"]
#1.del()根据下表删除
xb=int(input("请输入你要删除学生的下标"))
del names[xb]
for nam in names:
    print(nam)

#2.pop()删除最后一个元素
names.pop()
for nam in names:
    print(nam)

#3.remove()根据元素的值进行删除
sname=input("请输入您要删除的学生姓名")
names.remove(sname)
for nam in names:
    print(nam)