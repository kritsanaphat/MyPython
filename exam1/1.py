print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))
wind = ''
if(x>=0 and x<=51.99):
    wind = "Breeze."
elif(x>= 52 and x<=55.99):
    wind = "Depression."
elif(x>=56 and x<=101.99):
    wind = "Tropical Storm."
elif(x>=102 and x<=208.99):
    wind = "Typhoon."
elif(x>=209):
    wind = "Super Typhoon."
else:
    print("!!!Wrong value can't classify.")
if(wind is not ''):
    print("Wind classification is",wind)