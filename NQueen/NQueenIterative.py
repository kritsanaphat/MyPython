import time
start_time = time.time()

from itertools import permutations

N = input("Enter N : ")
N = int(N)

def print_table():
    for row in range(N):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(N):
            table[y][m] = 1
            table[m][x] = 1     
            table[y][x] = 2     
            test = table
            if y+m <= N-1 and x+m <= N-1:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= N-1:   
                table[y-m][x+m] = 1
            if y+m <= N-1 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False

table = [[0]*N for _ in range(N)]
numMem = []
for i in range(N):
    numMem.append(int(i))
perms = permutations(numMem)

num_comb = 0
numCheck = 0
for perm in perms:
    for i in range(N-1):
        if put_queen(perm[i], i) == True:
            numCheck += 1
            #print(numCheck)
    if(numCheck == N-1 and put_queen(perm[N-1], N-1) == True):
        print_table()
        num_comb += 1
        print(f"solution{num_comb}")
        print(" ")
        
    table = [[0] * N for _ in range(N)]
    numCheck = 0
    

print("Process finished --- %s seconds ---" % (time.time() - start_time))