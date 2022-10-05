string="7r5gg812"
C_str_lower=string.lower() #convert string to lower
C_str_list=list(C_str_lower) # convert that string to list
for i in range(len(C_str_list)):
    if C_str_list[i]>='a' and C_str_list[i]<='z':
        C_str_list[i]="@"
C_list_str="".join(C_str_list) #join all the characters in the list using join function
#print(c)  => 7@5@@812
c=C_list_str.split("@") #use split function to separate the numbers from the string
#print(c) => ['7','5','','812']
flag=0
for i in range(len(c)):
    if len(c[i])>1:
        r=len(c[i])//2
        d1=int(c[i][:r]) # 812 => 8 , 1234 => 12
        d2=int(c[i][r:]) # 812 => 12, 1234 => 34
        if d1%2==0 and d2%2==0:
            flag=1
if flag==1:
    print("true")
else:
    print("false")
