#use Recursion solve Palindrome
def Palindrome(n,t):
    if(t == 0):
        return 0
    elif(t>int((len(n)/2))):
        return Palindrome(n,t-1)-ord(n[t-1])
    else:
        return Palindrome(n,t-1)+ord(n[t-1])


x = input("Enter Input : ")
if(len(x)%2 == 0):
    if(Palindrome(x,len(x))==0):
        print("'",x,"'"," is palindrome",sep='')
    else:
        print("'",x,"'"," is not palindrome",sep='')
else:
    if(int(Palindrome(x,len(x))*(-1))==ord(x[int(len(x)/2)])):
        print("'",x,"'"," is palindrome",sep='')
    else:
        print("'",x,"'"," is not palindrome",sep='')
