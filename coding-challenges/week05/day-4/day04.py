#Array Rotation
# Given an array, rotate the array to the right by k steps, where k is non-negative.

arr=[1, 2, 3, 4, 5, 6, 7 ]
n=7
temp = []
i = -1
k = int(input("Enter steps:  "))
while (i >= -k):
   temp.append(arr[i])
   i = i - 1
print(temp+arr[:n-k])