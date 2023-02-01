def Spec2dignum(num):
    sum1,prod,temp=0,1,num
    while(num>0):
        sum1=sum1+num%10
        prod=prod*(num%10)
        num=num//10
    if (sum1+prod)==temp:
        return True
n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(n):
    if Spec2dignum(l[i]):
        count+=1
print(count)
