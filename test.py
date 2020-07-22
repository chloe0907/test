class Test1:
    def func1(self):
        print("func1")



class Person:
    # name = "default"

    @classmethod
    def setClassName(cls, name):
        cls.name = name

    def setName(self, name):
        self.name = name




    @staticmethod
    def getName():
        print("静态方法")


p = Person()
p.setName("chloe")
print(p.name)
#
#
Person.setClassName("DDDDDD")
print(Person.name)
print(Person.a)
#
# p.setClassName("AAAA")
# print(Person.name)
#
# Person.getName()
# p.getName()



