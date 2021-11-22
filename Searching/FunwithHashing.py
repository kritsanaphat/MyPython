class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,maxcollision):
        self.size = size
        self.currentcolloision = 0
        self.maxcolloision = maxcollision
        self.currentsize = 0
        self.data = []
        for i in range(size):
            self.data.append("None")
    def display(self):
        for i in range(self.size):
            print("#",i+1,"	",self.data[i],sep='')
        print("---------------------------")

    def insert(self,key,value):
        temp = 0
        for i in range(len(key)):
            temp += ord(key[i])
        index = temp%self.size
        if self.currentsize<self.size:
            if self.data[index] == "None":
                self.data[index] = Data(key,value)     
                self.display()
                self.currentsize +=1
                                            
            else:
                tempcolloision = 0
                while tempcolloision < self.maxcolloision:  
                        temp += (tempcolloision**2)
                        index2 = temp%self.size
                        if self.data[index2] == "None":
                            self.data[index2] = Data(key,value)     
                            self.display() 
                            self.currentsize +=1
                            break
                        else:
                            temp -= (tempcolloision**2)
                            self.currentcolloision +=1
                            print("collision number",tempcolloision+1,"at",index2)
                            tempcolloision += 1
                            if tempcolloision == self.maxcolloision:
                                print("Max of collisionChain")
                                self.display()
     
             
        else:
            if self.currentsize == self.size:
                print("This table is full !!!!!!")
            self.currentsize += 1
        
                        

print(" ***** Fun with hashing *****")
size,data = input("Enter Input : ").split('/')
data = data.replace(',',' ')
size = size.split()
data = data.split(" ")
H = hash(int(size[0]),int(size[1]))
i= 0

while(i<len(data)-1):
    H.insert(data[i],data[i+1])
    i += 2