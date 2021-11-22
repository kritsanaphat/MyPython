class Data:
    def __init__(self,data):
        self.data = data

    def __str__(self):
        return str(self.data)

class hash:
    def __init__(self,size,maxcollision,threshold):
        self.size = size
        self.threshold = threshold
        self.maxcolloision = maxcollision
        self.currentsize = 0
        self.currentthreshold = 0
        self.data = []
        self.tempdata = []
        print("Initial Table :")
        for i in range(size):
            self.data.append("None")
        self.display()
    def display(self):
        for i in range(self.size):
            print("#",i+1,"	",self.data[i],sep='')
        print("----------------------------------------")

    def insert(self,data,DisplayAdd,Displaytable):
        index = data%self.size
        if DisplayAdd:
                print("Add :",data)
        if ((self.currentsize+1)/self.size)*100 < self.threshold:
            
            if self.data[index] == "None":
               
                self.tempdata.append(data)
                self.data[index] = Data(data)
                self.currentsize +=1
                if Displaytable:
                    H.display()
            else:
                tempcolloision = 0
                while tempcolloision<self.maxcolloision:
                    
                    if self.data[index] == "None":
                        self.data[index] = Data(data)
                        if Displaytable:
                            self.display()
                        self.currentsize +=1
                        self.tempdata.append(data)
                        break
                    else:
                        print("collision number",tempcolloision+1,"at",index)
                        
                        tempcolloision +=1
                        index = (data+(tempcolloision**2))%self.size
                if tempcolloision == self.maxcolloision:
                        print("****** Max collision - Rehash !!! ******")
                        tempdataNow = data
                        self.data = []
                        newsize = (self.size*2)
                        flag = True
                        while flag:
                            flag = False
                            for i in range(2, newsize):
                                if (newsize % i) == 0:
                                    flag = True
                                    newsize +=1
                                    break
                                
                        self.size = newsize
                        for j in range(newsize):
                            self.data.append("None")
                        
                        j = 0
                        self.currentsize = 0
                        for k in range(len(self.tempdata)):
                            self.insert(int(self.tempdata[k]),False,False)
                            j += 1
                        
                        for i in range(j):
                            del self.tempdata[0]
                        
                        self.insert(tempdataNow,False,True)

        else:
            print("****** Data over threshold - Rehash !!! ******")
            tempdataNow = data
            self.data = []
            newsize = (self.size*2)
            flag = True
            while flag:
                flag = False
                for i in range(2, newsize):
                    if (newsize % i) == 0:
                        flag = True
                        newsize +=1
                        break
                    
            self.size = newsize
            for j in range(newsize):
                self.data.append("None")
            
            j = 0
            self.currentsize = 0
            for k in range(len(self.tempdata)):
                self.insert(int(self.tempdata[k]),False,False)
                j += 1
            
            for i in range(j):
                del self.tempdata[0]
            
            self.insert(tempdataNow,False,True)
      
        
        
        
                        

print(" ***** Rehashing *****")
size,data = input("Enter Input : ").split('/')
size = size.split()
data = data.split(" ")
H = hash(int(size[0]),int(size[1]),int(size[2]))

for i in data:
    H.insert(int(i),True,True)