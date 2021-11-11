class translator:
    

    def deciToRoman(self, num):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        x = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                x += syb[i]
                num -= val[i]
            i += 1
        return x
    
    def romanToDeci(self, s):
        s=s+'h'
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        dec =0
        i = 0
        while  s != 'e':
            for i in range(len(s)):
                if(s.rfind(syb[i])>0):
                    dec += val[i]
                    s.replace(syb[i], '')
            i += 1
        return dec


    

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))

