import math
print("*** multiplication or sum ***")
x,y= [int(x) for x in input("Enter num1 num2 : ").split()]
sum = x*y
if sum <= 1000:
    pass
else:
    sum=x+y
print("The result is",sum)
