a=int(input())
for i in range(0,a):
    for j in range(i+1):
        if i%2==0 and j%2==0:
           print("1 ",end="")
        elif i%2!=0 and j%2!=0:
            print("1 ",end="")
        else:
            print("0 ",end="")
    print(" ")    
