#task67
def coordinator(x,y):
    x=input("Enter a integer: ")
    y=input("Enter a integer: ")
    return(x,y)
my_coordinates= coordinator(5,6)
print(my_coordinates)
#task68
my_coordinates2= {}
def coordinator2(x,y):
    x=input("Enter a integer: ")
    y=input("Enter a integer: ")
    return(x,y)
my_coordinates2[coordinator2(0,0)] = "Home"
my_coordinates2[coordinator2(1,1)] = "Work"
my_coordinates2[coordinator2(-1,-1)] = "School"
for k,v in my_coordinates2.items():
 print(f"position: {k} name: {v}")
 #task69
def print_best_weapon(meele_weapon):
    best_damage = 0
    best_weapon_name = ""

    for weapon in meele_weapon:
        if weapon[1] > best_damage:
            best_damage = weapon[1]
            best_weapon_name = weapon[0]

    print(best_weapon_name)
weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]
print_best_weapon(meele_weapon)
#task70
game_table= [["_","_","_"],["_","_","_"],["_","_","_"]]
user_inputs=[]
def coordinator2():
    command=input("Please type new or exit: ")
    if command != "exit":
        x1=int(input("Enter a integer (row): "))
        y1=int(input("Enter a integer (col): "))
        return(x1,y1)    
    else:
        return "exit"
    
my_flag=True
while my_flag:
    result=coordinator2()
    if result== "exit":
        my_flag=False 
    else:
        user_inputs.append(result)

for(row,col) in user_inputs:
    game_table[row][col] = "*"

for row in game_table:
    print(row)
#task71
empty=set()
my_flag=True
while my_flag:
    user_inputs3=input("Enter an element for set: ")
    if user_inputs3== "exit":
        my_flag=False
        for i in empty:
            print(i)
    else:
        empty.add(user_inputs3)
#task72
empty2=set()
my_flag=True
while my_flag:
    user_inputs4=input("Enter an element for set: ")
    if user_inputs4 == empty2:
        print("This element is already in our set.")
    elif user_inputs4== "exit":
        my_flag=False
        for i in empty2:
            print(i)
    else:
        empty2.add(user_inputs4)
#task74
local=["my_ans"]
global=["real_age", "name" , "question", "user_guess"]
print(local)
print(global)
#task75
def start_game():
    score=10
    print(f"Game started! Current score: {score}")

def increase_score():
    score+= 5
    print(F"Score increased! Current score: {score}")

def display_score():
    print(f"Final score: {score}")

score=0
start_game()
increase_score()
display_score()
#task75
def start_game():
    global score
    score = 10
    print(f"Game started! Current score: {score}")

def increase_score():
    global score
    score+=5
    print(F"Score increased! Current score: {score}")

def display_score():
    print(f"Final score: {score}")

score=0
start_game()
increase_score()
display_score()
#task76
def age_calc():
    current_year = 2026
    my_flag = False
    while not my_flag:
        try:
            birthyear = int(input("What is your birthyear? "))
            my_flag = True
        except ValueError:
            print("Invalid Input.")
    return current_year - birthyear
print(f"You are {age_calc()} years old")
print("")
#task77
print("Bu kod SyntaxError verir. Çünkü genel expect en üstte olamaz")
x = int(input("Please enter a number: "))
my_flag = True
while my_flag:
    try:
        y = int(input("Please enter divider: "))
        print(f"{x} divided by {y} is {x / y}")
        my_flag = False
    except ZeroDivisionError:
        print("You can’t enter 0 as divider")
    except ValueError:
        print("Invalid Value")
    except:
        print("Some kind of error occured")
print("")
#task78
def new_game():
    name = input("game name: ")
    if name == "":
        raise ValueError("Name cannot be empty.")
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters.")

    try:
        year = int(input("release year: "))
    except ValueError:
        raise ValueError("Release year must be an integer.")

    if year < 0:
        raise ValueError("Release year cannot be negative.")
    if year > 2024:
        raise ValueError("Release year cannot be greater than 2024.")

    return (name, year)
game_list = []
flag = True
while flag:
    user_command = input("add or exit: ")
    if user_command == "exit":
        flag = False
    elif user_command == "add":
        try:
            game_list.append(new_game())
        except ValueError as e:
            print(e)
for game in game_list:
    print(f"Name: {game[0]}, Year: {game[1]}")
print("")
#task79
def factorial(n):
    if n < 0:
        raise ValueError("No negative value")
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k
try:
    print(factorial(5))
except ValueError as e:
    print(e)
try:
    print(factorial(-1))
except ValueError as e:
    print(e)