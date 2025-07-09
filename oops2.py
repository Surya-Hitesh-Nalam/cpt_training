#multiple inheritance
'''class base1(object): #first base class
    def __init__(self):
        super(base1,self).__init__()
        print("Base class-1")
class base2(object): #2nd base class
    def __init__(self):
        super(base2,self).__init__()
        print("Base class-2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("Derived class from both classes")
d=derived()'''

#Initialize classes addition,mul in a calc and pass the values from main program to the super class , where the sub classes add and mul were triggered and return the outputs respectively
'''
1. Take derived class - calc
2. from derived class call sub classes add and mul
3. return the values after math to the object
4. manual values of both numbers consider within the object'''
'''class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Addition class is also initialized by receiving a,b from object")
    def addition(self):
        return self.a+self.b
class mul:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Multiplication class is also initialized by receiving a and b")
    def multiplication(self):
        return self.a*self.b
class calc(add,mul):
    def __init__(self,a,b):
        add.__init__(self,a,b)
        mul.__init__(self,a,b)
        print("Calc class initialized")
x=int(input("enter first value:"))
y=int(input("enter second value:"))
c=calc(x,y)
print("sum:",c.addition())
print("mul:",c.multiplication())'''

'''class square:
    def __init__(self,a):
        self.a=a
    def sq(self):
        return self.a**2
class cube:
    def __init__(self,a):
        self.a=a
    def cu(self):
        return self.a**3

class derived(square,cube):
    def __init__(self,a):
        square.__init__(self,a)
        cube.__init__(self,a)
a=int(input("enter value:"))
b=derived(a)
print("answer:",b.sq()+b.cu())'''

#Multilevel inheritance
'''class student:
    def name(self):
        print("name:")
class teacher(student):
    def qualification(self):
        print("phd")
class hod(teacher):
    def exp(self):
        print("15 years")
head=hod()
head.name()
head.qualification()
head.exp()'''

#hierarchy inheritance

'''class number:
    def __init__(self,num):
        self.num=num
    def get_number(self):
        return self.num
class double(number):
    def result(self):
        return self.get_number()*2
class triple(number):
    def result(self):
        return self.get_number()*3
d=double(4)
print("double is:",d.result())
t=triple(4)
print("triple is:",t.result())'''

#Abstract Class
'''class fruit:
    def taste(self):
        raise NotImplementedError()
    def vitamin(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
    
class mango(fruit):
    def taste(self):
        return "sweet"
    def vitamin(self):
        return "viatmin-a"
    def color(self):
        return "yellow"
class orange(fruit):
    def taste(self):
        return "sour and sweet"
    def vitamin(self):
        return "viatmin-c"
    def color(self):
        return "orange"

alphanzo = mango()
print(alphanzo.taste(),alphanzo.vitamin(),alphanzo.color())
org=orange()
print(org.taste(),org.vitamin(),org.color())'''
















        
