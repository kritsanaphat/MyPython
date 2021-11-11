def hbd(age):
    y = 0
    s = 'saimai is just '
    s1 = ', in base '
    s2 = '!'

    if(age%2==0 and age!=0):
        age = age/2
        y=20
    else:
        age = (age/2)
        y=21
    age = int(age)
    y = str(y)
    age = str(age)
    return s+y+s1+age+s2

year = input("Enter year : ")

print(hbd(int(year)))