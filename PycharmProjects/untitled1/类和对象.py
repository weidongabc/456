class Dog:
    pass
#描述狗类的属性和行为
    #狗的属性
    #狗的毛色
    color='黑色'
    #狗的行为
    def run(self):
        return '狗跑的行为'
    def eat(self):
        return '狗吃的行为'
#创建狗类的一个实例
d=Dog()
d.age=2
print(d.eat())