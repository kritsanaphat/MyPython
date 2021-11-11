def weirdSubtract(n,k):
    i=0
    for i in range(k):
        if(n%10 ==0):
            n/=10
        else:
            n-=1
    n = int(n)
    return n

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))