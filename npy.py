import numpy as np
x=np.array([1,2,3,4,5])
# print("!-D array",x)

y=np.array([[1,2],[3,4]])
# print("2-D array",y)

z=np.zeros((2,3))
# print(z)

o=np.ones((2,3))
# print("ones",o)

i=np.eye(8)
# print("eye",i)

r = np.arange(0,11,2)
print("range",r)

seperate = np.linspace(0,1,5)
# print("linspace",seperate)


#Operations on arrays using array numpy
a1=np.array([1,2,3,4])
a2=np.array([4,5,6,7])
print("Addition",a1+a2)
print("Subtraction",a1-a2)
print("Multiplication",a1*a2)
print("Division",a1/a2)
print("Sin Values",np.sin(a1))
print("Mean",np.mean(a1))
print("Max",np.max(a1))
print("Min",np.min(a1))
print("Median",np.median(a1))

reshaped = a1.reshape((2,2))
print("Reshaped",reshaped)
linear = reshaped.reshape(-1)
print("Linear",linear)