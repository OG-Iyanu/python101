#checking if number is even.
num = 10
if num %2 == 0:
    print("The number is even")



#Display a message if a list is empty.
my_list = []
if len(my_list) == 0:
    print("The list is empty")
else:
    print("The list is empty")



#Write a script to check if a number as odd or even
num = 8
if num %2 == 0:
    print("The number is even")
else:
    print("The number is not odd")



#Write a script for Temp categories.
temp = 23.99
if temp <= 0:
    print('Its freezing cold!!!')
elif temp <= 10:
    print("Its cold")
elif temp <= 20:
    print('Its Moderate')
else:
    print("its hot")



#Print each character in a string.
skills = "james ward"
for i in skills:
   print(i)


#Create a list of squares of the first 10 natural numbers.
squares = [i**2 for i in range(1,11)]
print(squares)


#Add numbers until sum reaches 100.
total_sum = 0
current_number = 1
while total_sum < 100:
    total_sum += current_number
    current_number += 1
print('The sum of numbers until reaching 100 is:', total_sum)