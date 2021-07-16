#Q-1 ) Check if a number is Palindrome:
rev = 0
def Num_reverse(num):
   global rev
   if num!=0:
      rem=num%10
      rev=(rev*10)+rem
      Num_reverse(num//10)
      return rev
num=int(input("Enter your Number:"))
if(Num_reverse(num)==num):
   print("Palindrome Number is True.",num)
else:
   print(" Palindrome Number is False.",num)
    
    
#Q-2 ) Program for Sum of the digits of a given number:
# digit using recursion
def sum_of_digit( n ):
   if n == 0:
        return 0
   return (n % 10 + sum_of_digit(int(n / 10)))
 

num = int (input("Enter Number:"))
result = sum_of_digit(num)
print("Sum of digits in",num,"is", result)    

#Q-3 ) Given a number n, find sum of first n natural numbers:
def sum(num):
   if num<=0:
      return num
   return num+sum(num-1)
num=int(input("Enter the Number:"))      
print(sum(num)) 

#Q-4 ) [Bonus Question] Given two number x and y, find product using recursion.
def product(x,y):
    if(x<y):
        return product(y,x)
    elif(y!=0):
        return(x+product(x,y-1))
    else:
        return 0
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("Product is: ",product(x,y)
