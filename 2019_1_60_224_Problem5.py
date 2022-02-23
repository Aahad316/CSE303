

def prime_find_2019_1_60_224(N):
    for i in range(2, N+1, 1):
        if(N%i)==0:
            return False
            break  
        else:
          return True
      
N = int (input("Enter The Number: "))
if(prime_find_2019_1_60_224(N) == False):
    print(f'{N} is not a prime number')
else:
    print(f'{N} is a prime number')