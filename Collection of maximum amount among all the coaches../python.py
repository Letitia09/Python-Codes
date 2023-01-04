#Number_of_coaches
nc=int(input())#15
#Number_of_coaches_per_category
ncpc=list(map(int,input().split())))#[3,6,3,2,1]
Index=[1,2,3,4,5]
#No_of_seats_in_coach
nsc=list(map(int,input().split())))#[10,20,30,40,50]
Coach_code=['G','S','D','B','A']
#amount collected per category
acpc=[]
if nc<25:
    if 0 not in ncpc:
        for i in range(5):
            sum1=0
            for j in range(ncpc[i]):
                sum1=sum1 + (nsc[i]//(j+1))+(ord(Coach_code[i])*(i+1))
                #sum=sum+ nsc[i]/(i+1) + (ord(Coach_code[i])*Index[i]
            acpc.append(sum1)
print(max(acpc),"",sum(acpc)) # 1044 2905
#print(acpc)  : [231,1044,588,375]  
