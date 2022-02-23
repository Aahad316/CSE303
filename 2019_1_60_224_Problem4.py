

N = int(input("Enter Your Number: "))
i = 1
x = 2
sum = 0
print("The series is: ")
while i<=N:
    y = i**2
    print(y)
    sum = sum + y
    i=i+1
    
print(f'The Sum of the Series: {sum}')

