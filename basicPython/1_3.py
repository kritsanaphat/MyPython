print("*** Reading E-Book ***")
x,y= input("Text , Highlight : ").split(',')
if y in x:
        x=x.replace(y,"["+y+"]")

print(x)