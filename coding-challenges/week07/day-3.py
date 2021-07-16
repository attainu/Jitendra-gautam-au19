#Q-1 ) Recursive implementation of atoi() function:(

def myAtoiRecursive(string, num):
      
   if len(string) == 1:
      return int(string) + (num * 10)
          
    # add the next string item into our num value
   num = int(string[0:1]) + (num * 10)
      
    
   return myAtoiRecursive(string[1:], num)
  
string=input("Enter the no.") 
string+="1"   

  
print(myAtoiRecursive(string, 0))

#Q-2 ) Write a function that prints digits of a number from left to right , using
recursion
n = int(input())

def rec(n):
   if n==1:
        print(1)
   else:
      
      rec(n-1)
      print(n)

rec(n)

#Q-3 ) Reverse a string using recursion:
def rev_str(str1):
   if len(str1)==1:
      return str1
   else:
      return rev_str(str1[1:])+str1[0]
str1=input("Enter the String:")
str2=rev_str(str1)
print("Reverse string is:",str2)   
