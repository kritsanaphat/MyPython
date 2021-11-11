class MyInt:
    def __init__(self,num):
        self.dec = num
    def toRoman(self):
        num = self.dec
        Roman = str(self.dec)+" convert to Roman : "
        chrR = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        numR = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        while(num!=0 ):
            for i in range(len(chrR)):
                if num-numR[i] >= 0:
                    Roman += str(chrR[i])
                    num = num-numR[i]
                    break
        return  str(Roman)
    def __add__(self,x):
        s = str(a.dec)+' + '+str(b.dec)+' = '+str(int((a.dec+b.dec)+((a.dec+b.dec)*1/2)))
        return str(s)
    
print(" *** class MyInt ***")
x,y = (input("Enter 2 number : ").split())

a = MyInt(int(x))
b = MyInt(int(y))
print(a.toRoman())
print(b.toRoman())
print(a+b)


