# 1.Recursive Python  program to count the
# total number of vowels using recursion
 
# Function to check the Vowel
def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
 
# to count total number of
# vowel from 0 to n
def countVovels(str, n):
   if (n == 1):
      return isVowel(str[n - 1])
 
   return (countVovels(str, n - 1) +
               isVowel(str[n - 1]))
 
 
# string object
str = "Jitendra"
 
# Total numbers of Vowel
print(countVovels(str, len(str)))


#Question 2. Write a program to find the fibonacci number in a string
n = int(input("Enter number you whant in this series:"))
first = 0
second = 1
for i in range(n):
   print(first)
   temp = first
   first = second
   second = temp+second
  
# 3.Python program to calculate length of a string using recursion
str = "Software Engineer"
# calculate length
def string_len(str) :
   if str == '':
      return 0
   else:
      return 1 + string_len(str[1:])
print (string_len(str))

#Question 4. Write a program using recursion to find the sum of first N natural number.

def sum (n):
   if n==1:
      return 1
   else:
      return n+sum(n-1)
n=int(input("Enter Natural Number:"))
if n<=0:
   print("Not a natural number.." )
else:         
   print("Sum of series:",sum(n))
    
#Questions 5. Write a program to compute the power of a number eg pow(n, 5) will give
#you n to the power 5. Use recursion in it.

def power(n,p):
   if p==0:
      return 1
   else:
      n*=power(n,p-1)
      return n 
n=int(input("Enter number:"))
p=5  # p=power or Exponent      
print(power(n,p))     
