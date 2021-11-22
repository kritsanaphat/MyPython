def Data(name,wins,loss,draws,scored,conceded):
    point = []
    gD = []
    for i in range(len(name)):
        point.insert(i,pointT(wins[i],draws[i]))
        gD.insert(i,scored[i]-conceded[i])
    name,point,gD = findWinBypoint(name,point,0,gD)
    if isduplicate(point,0):
        name,point,gD = findWinByGD(name,point,gD,0)
    return name,point,gD
    
def isduplicate(num,count):
    if count == len(num)-1:
        return False
    else:
        if count<len(num)-1:
            if int(num[count]) != int(num[count+1]):
                return isduplicate(num,count+1)
            else:
                return True

def pointT(win,draws):
    return (win*3)+(draws)

def findWinBypoint(name,point,count,gD):
    if count<len(point)-1:
        if point[count]<point[count+1]:
            temp = point[count+1]
            tempN = name[count+1]
            tempgD = gD[count+1]
            point[count+1] = point[count]
            name[count+1] = name[count]
            gD[count+1]= gD[count]
            point[count] = temp
            name[count] = tempN
            gD[count] = tempgD
            count = 0
            return findWinBypoint(name,point,0,gD)
        else:
            return findWinBypoint(name,point,count+1,gD)
    else:
        return name,point,gD

def findWinByGD(name,point,gD,count):
    if count<len(gD)-1:
        if gD[count]<gD[count+1] and point[count]<=point[count+1]:
            temp = gD[count+1]
            tempN = name[count+1]
            tempP = point[count+1]
            gD[count+1] = gD[count]
            name[count+1] = name[count]
            gD[count] = temp
            name[count] = tempN
            point[count] = tempP
            count = 0
            return findWinByGD(name,point,gD,0)
        else:
            return findWinByGD(name,point,gD,count+1)
    else:
        return name,point,gD

    

inp =input("Enter Input : ")
inp = inp.replace('/',",")
inp = inp.split(',')
name=[] 
wins=[] 
loss=[] 
draws=[] 
scored=[] 
conceded=[]

for i in range(0,int(len(inp)),6):
    name.append(inp[i])
    wins.append(int(inp[i+1]))
    loss.append(inp[i+2])
    draws.append(int(inp[i+3]))
    scored.append(int(inp[i+4]))
    conceded.append(int(inp[i+5]))


name,point,gD= Data(name,wins,loss,draws,scored,conceded)
print("== results ==")
for i in range(len(name)):
     print("['",name[i],"', {'points': ",point[i],"}, {'gd': ",gD[i],"}]",sep='')
     