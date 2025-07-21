'''data = [10,'hi',4.5,'students',3,100]
#'From the list containing numbers and strings , extract only integers using lambda function and list comprehension [o/p]:[10,3,100]'
res = [x for x in data if (lambda x: type(x) == int)(x)]
print(res)'''

#calculate the factorial of n using recursion of lambda function n=4
#res = (lambda x: 1 if x==1 else x* res(x-1))
'''fact = (lambda f: lambda n: 1 if n==0 else n*f(f)(n-1))(lambda f: lambda n:1 if n==0 else n*f(f)(n-1))
#print(res(4))
print(fact(4))

#sum of digits: 3456 op: 15 using lambda functions
sum_of_digits = (lambda f: lambda n : 0 if n==0 else n%10 + f(f)(n//10))(lambda f: lambda n: 0 if n==0 else n%10+ f(f)(n//10))
print(sum_of_digits(3456))

x= lambda a: a+22
print(x(10))

big = lambda x,y : x if x>y else y
print(big(10,20))
'''
'''
nums = [11,22,33,44,55,66,77,88,99]
e= list(filter(lambda x:x%2==0,nums))
print(e)
packs = [(11,99),(2,11),(66,88)]
res = sorted(packs, key=lambda x: x[1])
print(res)

def b(n):
    return lambda x: x*n
a=b(2)
print(a(5))

def a(n):
    return n**3
b=lambda x:x**3

#print(a(2))
#print(b(2))
'''
'''code to declare longest string using lambda '''
'''
long = lambda x, y: x if len(x) > len(y) else y
#print(long('Surya','Hitesh'))

data = ['pen','cap','bat']
upper = [(lambda x: x.upper())(d) for d in data]
#print(upper)
'''
'''reversing a string using lambda and list comprehension'''

'''words=['hello', 'world', 'python']

rev = (lambda x: x[::-1])([word for word in words])
print(rev)

l=['hi','','students','','bye']
# use list comprehension and lamda to remove empty strings from the list
non_empty =''.join([x for x in l if (lambda x: x!='')(x)])

n = (lambda x: x)([x for x in l if x != ''])
print(n)'''


'''(a+b)*c expression lambda evaluate and returns toa nother lambda '''

'''l2 = lambda a: lambda b,c: (a+b)*c
l1 = l2(2)
value = l1(1,3)
print(value)'''

#l2 = (lambda a: lambda b,c: ((a+b)*c))(5)(3,2)

#l2 = (lambda a: lambda b: lambda c,d : (a+b)*(c+d))(2)(3)(4,5)

#(a-b)//(c-d)
'''try:
    l2 = (lambda a: lambda b: lambda c,d: (a-b)//(c-d))(2)(2)(5,4)
    print(l2)
except:
    print("error occured")'''

'''num = int(input("a:"))
n= int(input("b:"))
oper = lambda a: lambda x:(x+a)**2
numsq = oper(num)
print(numsq(n))'''

'''try:
    l2 = (lambda a:lambda b: lambda c,d: (a-b)/(c-d))(2)(1)(5,5)
    print(l2)
except ZeroDivisionError:
    print("Error")
except TypeError:
    print("Type Error")'''

'''l2 = (lambda a:lambda b: lambda c,d:a+'-'+b+'-'+c+'-'+d)("hi")("Students")("Good","Morning")
print(l2)'''

'''given atrributed a,b,c,d are hi,!,students , !!!! write a nested lambda to concatinate the abcd , by converting a and c to uppercase
output: HISTUDENT!!!'''

l2 = (lambda a:lambda b: lambda c,d:a.upper()+'-'+b+'-'+c.upper()+'-'+d)("hi")("Students")("Good","Morning")
print(l2)

'''given attributes a,b,c,d are hi,hello,students,teachers ||| write a nested lambda to concatnate abcd , by reversing with seperator'''

l2 = (lambda a:lambda b: lambda c,d:a[::-1]+'-'+b[::-1]+'-'+c[::-1]+'-'+d[::-1])("hi")("Students")("Good","Morning")
print(l2)

'''numbers = lambda x:lambda a:a*2 if a>x else:a*3
above_5 = numbers(5)
num=[4,6,3,8]
o=list(map(above_5,num))
print(o)'''