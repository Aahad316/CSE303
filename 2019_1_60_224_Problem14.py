
def palindrome_checker_2019_1_60_224(palin):
    
       if palin == palin[::-1]:
         return True
       
palin = input("Enter your word: ")

if palindrome_checker_2019_1_60_224(palin) == True:
    
          print(f'{palin} is a palindrome')
else:
    print(f'{palin} is not a palindrome')