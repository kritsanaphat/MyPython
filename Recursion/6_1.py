#use Recursion solve Fibonacci
def fibR(n):    # recursive, n>=0
    if n <= 1:
        return n
    else:
        return fibR(n-1) + fibR(n-2)
x = int(input("Enter Number : "))
print(fibR(x))
