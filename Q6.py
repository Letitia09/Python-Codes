a=int(input())
b=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i,len(l)):
        sum=l[i]+l[j]
        if sum==a:
            print("{0} + {1} = {2}".format(l[i],l[j],sum))
