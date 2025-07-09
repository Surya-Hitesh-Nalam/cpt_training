#OOPS

#Class And Object
'''class abc():
    var=100
    def display(self):
        print("This is a class method")
obj=abc()
print(obj.var)
obj.display()'''

#Constructor
'''class abc():
    def __init__(self,val):
        self.val=val
        print("this is a class method")
        print("value is :",val)
    def display(self):
        print("The value is:",val)
obj=abc(5)
obj.display()'''

#Class Obj Variable
'''class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("Object var:",var)
        print("Class var:",abc.cv)
obj=abc(10)
obj=abc(20)
obj=abc(30)'''

#Code to illustrate the modification of an instance variable to check whether the passing attribute is even or odd, by creating a class number and function to check even or odd
'''class abc:
    even=0
    def check(self,val):
        if val%2==0:
            self.even=1
    def eo(self,val):
        self.check(val)
        if self.even==1:
            print("Given val is even")
        else:
            print("Given val is odd")
val=int(input("enter a number:"))
obj=abc()
obj.eo(val)'''


#Segregate the even or odd parameters in a list and print even list and odd list seperately using class number"
'''
class abc:
    odd=[]
    even=[]
    def __init__(self,val):
        if val%2==0:
            abc.even.append(val)
        else:
            abc.odd.append(val)

n1=abc(21)
n2=abc(32)
n3=abc(43)
n4=abc(54)
n5=abc(65)
print(abc.even)
print(abc.odd)'''

#Delete Vars
'''class abc:
'''

#Class Methods
'''__repr__
__cmp__
__len__'''

'''class abc:
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj=abc("abcdef",10)
print("The value stored in object is :",repr(obj))
print("The length of name stored in object :",len(obj))
obj1=abc("ghij",1)
val=obj.__cmp__(obj1)
if val==0:
    print("Both are equal")
elif val==-1:
    print("First values is less than second")
else:
    print("Second value is less than first")
'''
#Advanced class methods
'''
1.__call__() -> Instance can be directly called
2.__lt__(),__le__(),__gt__(),__ge__(),__eq__(),__ne__()
3.__hash__() -> decide obj/set/dict
4.__iter__() -> Iterate the objects
5.__getitem__(),__setitem__()
'''
class number():
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=number([1,2,3,4,5,6,7,8,9])
print(numlist)
numlist[3]=10
print(numlist.mylist)
                    





