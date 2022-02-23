
n = int(input("Enter your number: "))
F0 = 0
F1 = 1
for i in range(2, n):
            F =F0 + F1
            F0 = F1
            F1 = F
        
print(f'The {n}th fibonacci number is {F1}')
