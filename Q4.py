a=int(input())
l=list(map(int,input().split()))
p=1
sum=0
for i in range(len(l)):
    sum=sum+l[i]
    p=p*l[i]
if sum%2==0:
    print(sum)
else:
    print(p)
    
