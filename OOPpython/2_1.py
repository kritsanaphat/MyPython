class translator:
    

    def deciToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        x= ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                x += syb[i]
                num -= val[i]
            i += 1

        return x
      
            

    def romanToDeci(self, s):
        s = s + "e"
        x=0
        i=0
        
        while(s[i]!="e"):
            if(s[i]=="M"):
                x = x+1000
                i+=1 
                
                
            elif(s[i]=="D"):
                x =x +500
                i+=1
                
            
            elif(s[i]=="C"):
                if(s[i+1]=="D"):
                    x= x+400
                    i+=2
                elif(s[i+1]=="M"):
                    x=x+900
                    i+=2 
                else:
                    x=x+100
                    i+=1

            elif(s[i]=="L"):
                x =x +50
                i+=1
                
            elif(s[i]=="C"):
                x =x +100
                i+=1
                
            elif(s[i]=="X"):
                if(s[i+1]=="L"):
                    x= x+40
                    i+=2
                    
                elif(s[i+1]=="C"):
                    x=x+90
                    i+=2
                                      
                else:
                    x=x+10
                    i+=1
                   

            elif(s[i]=="V"):
                x =x +5
                i+=1
                
            
            elif(s[i]=="X"):
                x =x +10
                i+=1
                
                
            elif(s[i]=="I"):
                if(s[i+1]=="V"):
                    x= x+4
                    i+=2   
                elif(s[i+1]=="X"):
                    x=x+9
                    i+=2   
                else:
                    x=x+1
                    i+=1
                  
           
        

        return x
        
      

num = int(input("Enter number to translate : "))


print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))
