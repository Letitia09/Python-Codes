def sub_lists (l):
	lists = [[]]  #lists=[]
	for i in range(len(l) + 1):
		for j in range(i):
			lists.append(l[j: i])
	return lists

def Answer(l):
  c=sub_lists(l)
  count=0
  for i in range(len(c)):
    if 'a' in c[i] and 'b' in c[i]and 'c' in c[i]:
        count +=1
  print(len(c)-count-1) # -1 is for included because they said that the substring should not be an empty string
  # if lists=[] under sub_lists function then print statement must be print(len(c)-count) to reduce one iteration in Answer function, as the substring should not be an empty string is included in the question
      
l = input()
Answer(l)

