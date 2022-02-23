

l1=[10,25,35,40,50,61,70,88,93,101]
l2=[85,96,69,53,62,78,82,16,27,58]
new_list=[]
for i in range(0,len(l1)):
    n=l1[i]
    if(n%2!=0):
        new_list.append(n)
for i in range(0,len(l2)):
    x=l2[i]
    if(x%2==0):
        new_list.append(x)

print(f'The new list is {new_list}')