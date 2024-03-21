'''
# else:
     print("not eligible")

# ! Eg:3
# ? take values of length and breadth of a
# ? from user and check if it is squre or not.

#length = int(input())
#breadth = int(input())
# if length==breadth:
      print("its a square")
# else:
      print("its not square")

# Eg:4
  # python program to check whether the
  # given integer is a multiple of both 5 and 7
  n = int(input("enter the number"))
  if n%5==0 and n%7==0:
      print("yes")
  else:
      print("no")
'''
'''
# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following ceiteria :

#          cost price (in Rs)                              Tax
#          > 100000                                         15% + discount 6%
#           <100000                                         5%

price = int(input("enter the price:"))
amount = 0
if price>=100000:
    discount = 100000*(6/100)
    value = price-discount
    amount=value*(15/100)
    total=value+tax
#else:
#    tax = price*(5/100)
#    total = price+tax
# print("The onroad cost of bike is:",total)



# if elif
     # Eg:1
#        a = 7
#       b = 9
#       c = 3

# if a>b and a>c:
#      print("A is greater")
# elif b>a and b>c:
#     print("c is greater")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.


# mark = int(input("enter mark:"))
# if mark>=80 and mark<<=100:
#     print("A")
# elif mark >=60 and mark<80:
       print("B")
# elif mark>=50 and mark<60:
       print("C")
# elif mark >=40 and mark<50:
       print("D")
# else:
#    print("Faile")

# Eg:6
# ? Accept the age of 4 people and display the oldest one.

# ! ---> short hand if else
# Eg:1
#  a = 9
#  b = 60
# if a>b:
#      print("A")
# else:
#     print("B")
# ? ---> using short hand if else
# * Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.) always it have to end with else

# print("A") if a>b else print("B")


# ! code to check the given char is vowel or consonent
# cnar = input("enter the cnar:")
# if char=="a" 0r char --'e' or char --'o' or char --'u':
#        print("its vowel")
# else:
#     print("its consonent")


# ? or
# str1 = "aeiouAEIOU"
# if char in str1:
#      print("vowel")
# else:
#     print("consonent")


# ! shathand if else
# char = input("enter the char:")
# str1 = "aeiouAEIOU"
# print("vowels") if char in str1 else print("consonent")


# ! -----> elif ladder using shart hand if else
# Eg:1
# ? find greatest among 3 variables using shart hand if else
# a = 8
# b = 5
# c = 9

# print("A os greater") if a>b and a>c else print("B is greater")
# if b>a and b>c else print("C is greater")

# ! -----------> looping

# looping can be implimented using
# for loop
# while loop

# ----> for loop
# ? for loop is used for iteration, if we know the number of times the loop have to run
# ? It is used to iterate the iterables eg(string,tuple,list,etc....)


# Todo ----> syntax for loop
# ! for syntax in c
# for (i=0:i<10:i++){
#      print(:"hello"):
# }

# ! for syntax in python
# for user defined variable in range(start,end,step): defult step value is 1
#   statement
#   statement
#   statement

# ? Eg:1
# To print the value from 1 to 10 using for loop
# for i in range(0,10): #(n,n-1)
#     print(i)
#     print("hello")

# Eg:2
# for value in range(1,15,2):
#      print("value")

# for value in range(1,15,3):
#     print("value")

# Eg:3
# To decrement the value

# for value in range(10,-0,-1):
#      print("value")

# for value in range(10, 0 ,-2):
#     print("value")

# for value in range(10, 0, 1):
#     print("value") # no output


# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
for i in range(23,43+1):
    print(i*7)



    ans="7 x {}={}"
    print(ans.format(i,i*7))

    print(f"7 x {i}={i*7}")

# Eg:5
# break ---> used to terminate the loop

for i in range(1,10):
    print(i)
    if i ==6:
        break
    print(i)

# ? Eg:6
# for val in range(1,10):
#    if val==6:
#       print(val)
#       break

# ? Eg:7
# for val in range(1,10):
#     if val==6:
#        print(val)
#        break


# ! continue
# Eg:1
for i in range(1,10):
    if i ==6:
        continue
    print(i)


# practise problems
# ? print the even number between 20 to 40.
# for i in range(20,41,2):
#    if i %2==0:
#        print(i)

# 1 -----> while loop
# ? while is used when we do not know the number of times the loop have to run
# ? TO iterate the non iterable element while loop is used.

# Todo syntax

# initiailisation
# while condition:
#       statement
#       incre or decre
'''

#! Eg:1
# to iterate number from 1 to 10
i=0
while i<11:
    print(1)
    i=i+1

                                                                                                                



