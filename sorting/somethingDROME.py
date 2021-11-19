def Maxmin(num,count):
    if count == len(num)-1:
        return True
    else:
        if count<len(num)-1:
            if int(num[count])>= int(num[count+1]):
                return Maxmin(num,count+1)
            else:
                return False

def Minmax(num,count):
    if count == len(num)-1:
        return True
    else:
        if count<len(num)-1:
            if int(num[count])<= int(num[count+1]):
                return Minmax(num,count+1)
            else:
                return False

def isduplicate(num,count):
    if count == len(num)-1:
        return False
    else:
        if count<len(num)-1:
            if int(num[count]) != int(num[count+1]):
                return isduplicate(num,count+1)
            else:
                return True

def SameAll(num,count):
    if count == len(num)-1:
        return True
    else:
        if count<len(num)-1:
            if int(num[count]) == int(num[count+1]):
                return SameAll(num,count+1)
            else:
                return False

inp = input('Enter Input : ')
inp = list(inp)
op1= Maxmin(inp,0)
op2 = Minmax(inp,0)
op3 = isduplicate(inp,0)
op4 = SameAll(inp,0)
if op2 and not op3 and not op4:
    print("Metadrome")
elif op2 and op3 and not op4:
    print("Plaindrome")
elif op1 and  not op3 and not op4:
    print("Katadrome")
elif op1 and op3 and not op4:
    print("Nialpdrome")
elif op4:
    print("Repdrome")
else:
    print("Nondrome")