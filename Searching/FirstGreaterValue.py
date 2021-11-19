def FristGreaterValue(l, r, arr, x):
    if r< len(x):
            if int(x[r]) < arr[l]:
                if int(x[r]) != len(x)-1:
                    print(arr[l])
                    return FristGreaterValue(0,r+1,arr,x)
                else:
                    print(arr[l])
            elif l != len(arr)-1:
                return  FristGreaterValue(l+1,r,arr,x)
            else:
                print("No First Greater Value")

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(inp[1].split())
FristGreaterValue(0,0, sorted(arr), k)
