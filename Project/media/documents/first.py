import subprocess

class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def getEmployee(self):
        print("EMplyee id :%d and name is:%s"%(self.id,self.name))

e=Employee(1,"Pranav")
e.getEmployee()




class a:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")

class c:
    def feature5(self):
        print("feature 5working")
    def feature2(self):
        print("feature 6working")

class b(a,c):
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")


B=b()
B.feature1()
B.feature2()
B.feature3()
B.feature4()
B.feature5()
class VbStudio:
    def execute(self):
        print("Complile as well as it runs gret")
class Pycharm:
    def execute(self):
        print("good intrepretor")

class Laptop:
    def code(self,ide):
        ide.execute()


ide=VbStudio()
l=Laptop()
l.code(ide)    

class A:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print("Name is %s and id is %d"%(self.name,self.id))

    def __str__(self):
        return '{},{}'.format(self.num1 , self.num2)





def fact(num):
    if num ==0:
        return 1
    else:
      return num * fact(num-1)

print(fact(5))


def one():

     uname="uname"
     uname_arg="-a"
     subprocess.call([uname,uname_arg])

print(one())

