a=int(input())
l=[]
for i in range(a):
    x=int(input())
    l.append(x)
codd=0
ceven=0
for i in range(a):
    if l[i]%2==0:
        ceven+=1
    else:
        codd+=1
print("{0} {1}".format(ceven,codd))
