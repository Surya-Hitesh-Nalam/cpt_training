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
'''nums = [11,22,33,44,55,66,77,88,99]
e= list(filter(lambda x:x%2==0,nums))
print(e)'''

'''
packs = [(11,99),(2,11),(66,88)]
res = sorted(packs, key=lambda x: x[1])
print(res)

def b(n):
    return lambda x: x*n
a=b(2)
print(a(5))'''

def a(n):
    return n**3
b=lambda x:x**3

#print(a(2))
#print(b(2))

'''code to declare longest string using lambda '''

long = lambda x, y: x if len(x) > len(y) else y
#print(long('Surya','Hitesh'))

data = ['pen','cap','bat']
upper = [(lambda x: x.upper())(d) for d in data]
#print(upper)

'''reversing a string using lambda and list comprehension'''
words=['hello', 'world', 'python']

rev = (lambda x: x[::-1])([word for word in words])
print(rev)

l=['hi','','students','','bye']
# use list comprehension and lamda to remove empty strings from the list
non_empty =''.join([x for x in l if (lambda x: x!='')(x)])

n = (lambda x: x)([x for x in l if x != ''])
print(n)