

def largest_number_2019_1_60_224(l):
    max=-99999999999
    for i in range(0, len(list)):
        if(l[i]>max):
            max = l[i]
    return max

def smallest_number_2019_1_60_224(l):
    
    min=99999999999
    for i in range(0, len(list)):
        if(l[i]<min):
            min = l[i]
    return min

list=[10,20,30,40,50,60,70,80,90,100]

print(f'The largest number from the list is: {largest_number_2019_1_60_224(list)}')
print(f'The smallest number from the list is: {smallest_number_2019_1_60_224(list)}')