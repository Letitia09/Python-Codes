a=int(input())
for i in range(a+4):
    for j in range(a+4):
        if j==5 or i==5:
           print("*",end="")
        else:
            print(" ",end="")
    print("  ")
