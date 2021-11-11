
def mod_position(arr, s):
    s=int(s)
    text =[]
    i=0
    while(i<len(arr)):
        if((i+1)%s==0):
            text.append(arr[i])
        i+=1
    return text
        

print("*** Mod Position ***")
n,s = input("Enter Input : ").split(',')
print(mod_position(n,s))
