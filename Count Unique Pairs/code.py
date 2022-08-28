#using lists and sets => METHOD 1
a=int(input())
b=list(map(int,input().split()))
c=list(set(b))
l=[]
for i in range(len(c)):
    for j in range(len(c)):
        l.append((c[i],c[j]))
print(len(l))  

#using sets => METHOD 2
a=int(input())
b=list(map(int,input().split()))
s=set()
for i in range(len(b)):
    for j in range(len(b)):
        s.add((b[i],b[j]))
print(len(s))  
