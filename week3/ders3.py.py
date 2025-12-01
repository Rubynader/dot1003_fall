#task21
def greeting(name):
    print(f"Hello {name}")
user_input=input("Please enter your name:")
greeting(user_input)

#task22
def greeting(name):
    return f"Hello {name}"
user_input=input("Please enter your name:")
print(greeting(user_input))

#task23
def sum(num1 , num2):
    return num1 + num2
user_input1=int(input("Please enter a first number: "))
user_input2=int(input("Please enter a second number: "))
print(sum(user_input1,user_input2))     

#task24
name= "Gordon Freeman"
def greeting(input_name):
    print(f"Hi {input_name}")
greeting("Andrew Ryan")
greeting("Gordon Freeman")

#task25
def mean(num3 , num4 , num5):
    return (num3 + num4 + num5)/3
user_input3=int(input("Please enter a first number: "))
user_input4=int(input("Please enter a second number: "))
user_input5=int(input("Please enter a third number: "))
print(mean(user_input3,user_input4,user_input5))

#task26
my_flag=True
while my_flag:
     my_name=input("Say my name: ")
     if my_name == "Heisenberg":       
       print("You're goddamn right.")
       my_flag=False
       
#task27
my_flag1 = True
password = input("Enter your password: ")

while my_flag1:
    password1 = input("Enter again: ")
    if password1 == password:
        print("Your password matches and account created successfully.")
        my_flag1 = False
    else:
        print("They are not same. Try again.")

#task28
number2=int(input("Enter a start number: "))
my_flag2=True
while my_flag2: 
    print(number2)
    number2=number2 -1
    if number2 == 0:
       print("Kaboom!")
       my_flag2=False
 
#task29
my_flag3=True
password2=123456
attempts=3 
while my_flag3:
    user_input=int(input("Enter your password: "))
    attempts= attempts - 1
    if user_input == password2:
      my_flag3=False
      print("Welcome!")
       
    elif attempts == 0:    
     my_flag3:False
     print("Incorrect Password. Exterminate... ") 

    elif user_input != password2:
     print("Try Again")

#task30
my_flag4=True
totalnumber=0
even=0
odd=0
number=0
print("dumb calculator v0.1 if you want to exit, enter 0")
while my_flag4:
    number1=int(input("Please enter a number: "))
    if number1==0:
       my_flag4=False
    mean=number/totalnumber
    print("Total Number: {totalnumber}")
    print("Sum: {number}")
    print("Mean: {mean}")
    print("Odd: {odd}  Even: {even}")
else:
    number=number1+number
    totalnumber=totalnumber + 1
    if number1%2==0:
        even=even + 1
    else:
        odd=odd + 1    

#task31
my_list=[]
my_list.append(2)
my_list.append(4)
my_list.append(6)
print(my_list)
print(my_list[0])
print("List lenght is" + len(my_list))
print(my_list[1] , my_list[-1])

#task32
my_list2=[]
my_list2.append(2)
my_list2.append(3)
my_list2.append(5)
print(my_list2)
my_list2[0]=1
print(my_list2)

#task33
my_list3 = []
my_flag=True
while my_flag: 
    user_input6 = input("Please enter an input (if you want to exit, enter exit): ")
    if user_input6 == "exit":
        my_flag=False 
    if my_flag:
        my_list3.append(user_input6)
print(my_list3)

#task34
my_list3 = []
my_flag=True
while my_flag: 
    user_input6 = input("Please enter an input (if you want to exit, enter exit): ")
    if user_input6 == "exit":
        my_flag=False 
    if my_flag:
        my_list3.append(user_input6)
print(my_list3)

for i in my_list3:
    print(i) 

#task35
user_input7=input("Please enter an input: ")
for char in user_input:
    print(char)

#task36
raw_points1=[1,2,1,3]
total_points1=0
for p in raw_points1:
    total_points1 += p
print(f"total {total_points} points earned")
 
 #task37
total_points2 = 0
raw_points2=[1,-2,1,3,-5,7,0]
for num in raw_points:
    if num > 0:      
        total_points += num

print(f"total {total_points} points earned")

#task38
size = int(input("Enter a table size: "))
for i in range(size):
    print("|" + "_|" * size)

#task39
height = int(input("Spruce height: "))
for i in range(height):
    spaces = " " * (height - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
print(" " * height + "*")