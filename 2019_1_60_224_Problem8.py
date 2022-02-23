list=[10,20,30,40,50,60,70,80,90,100]

Sum = 0

for i in range(0, len(list),2):
    Sum = Sum + list[i]
    

print(f'The sum of the even-indexed elements {Sum}')