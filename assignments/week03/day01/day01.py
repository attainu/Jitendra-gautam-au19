#Write a program to print numbers from 1 to N where N is input from user, but prints
#"Fizz" for multiple of 3, "Buzz" for multiple of 5 and "FizzBuzz" for multiple of both
n = int(input("Give Number : "))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
       print(i)