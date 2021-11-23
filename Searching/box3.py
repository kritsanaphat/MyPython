def Min(inp,box,weigth):
    index = 0
    for i in range(box):
        box2 = 0
        while True:
            if index == len(inp):
                return True
            
            if weigth >= inp[index] + box2:
                box2 += inp[index]
                index += 1
            else:
                break

    return False 

x = input("Enter Input : ").split("/")
n = [int(i) for i in x[0].split()]
numbox = int(x[1])
weigth = 0
for j in n:
    if j > weigth:
        weigth = j
while Min(n,numbox,weigth) is False:
    weigth += 1

print(f"Minimum weigth for {numbox} box(es) = {weigth}")