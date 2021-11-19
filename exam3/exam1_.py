def harmonic_sum(n):
    if n==1:
        print("1",end='')
        return n
    else:
        num =1/n+harmonic_sum(n-1)
        print(" + 1/"+str(n),end='')
    return num
print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
print(" = %.8f" %(harmonic_sum(num)))