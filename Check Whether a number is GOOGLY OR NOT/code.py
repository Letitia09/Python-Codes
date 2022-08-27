a=int(input())
b=str(a)
sum=0
for i in range(len(b)):
    sum=sum+int(b[i])
if sum > 1:
   for i in range(2,sum):
       if (sum % i) == 0:
           print("NOT GOOGLY")
           break
   else:
       print("GOOGLY")
else:
   print("NOT GOOGLY")
