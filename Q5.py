a=int(input())
l=list(map(int,input().split()))
counteven=0
countodd=0
for i in range(len(l)):
    if l[i]%2==0:
        counteven+=1
    else:
        countodd+=1
print("Number of even numbers :",counteven)
print("Number of odd numbers :",countodd)
