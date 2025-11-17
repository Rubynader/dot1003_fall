print("Robins will wear their feathery fire")
print("Whistling their whims on a low fence-wire; ")
print("And not one will know of the war, ")
print("not one")
print("")
print(f"Hours in a week : {24 * 7}" )
print(f"Minutes in a week :{(24 * 60 * 7)}")
print(f"Seconds in a week :{24 * 7 * 60 * 60}")
print("")
name=input("What is your name?")
email=input("What is your email address?")
nickname=input("What is your nickname?")
print("Your name= "+ name)
print("Your email address="+email)
print("Your nickname="+nickname)
print("")
user1=input("enter a name: ")
user2=input("enter a name too: ")
print(f"Thank you, {user1}")
print(f"But our {user2} is in another castle!")
print("")
name2= "Courier"
age= 34
city= "New Vegas"
print(f"Hi {name2}, you are {age} years old. You live in {city}.")
print("")
name3= "Ozan Akyol"
age2= 18
skill1= "python"
level1= "beginner"
skill2= "2d art"
level2= "beginner"
lower= 2000
upper= 3000
print(f"My name is {name3}, I am {age2} years old")
print("")
print("My skills are")
print(f"- {skill1} ({level1})")
print(f"- {skill2} ({level2})")
print("")
print(f"My salary expectation is {lower}-{upper} euros/month")
print("")
num1=3
num2=5
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")
print("")
weight=float(input("enter your weight: "))
height= float(input("enter your height: "))
print(f"Your BMI is {weight/(height*height)}")
print("")
gamename=input("enter a game name ")
gamereleased=input("Which year was this game released?")
print(f"{gamename} is {2025-int(gamereleased)} years old.")
print("")
number=int(input("Please type in the first number"))
number1=int(input("Please type in the second number"))
number2=int(input("Please type in the third number"))
product= number * number1 * number2
print(f"The product is {product}")
print("")
weekly_eat_cafe=int(input("How many times a week do you eat at the cafeteria?"))
price_lunch=int(input("The price of a typical student lunch?"))
price_groceries=int(input("How much mony do you spend on groceries in a week?"))
print("")
print("Average food expenditure: ")
daily_lunch=float(price_lunch*weekly_eat_cafe/7)
daily_groceries=float(price_groceries/7)
print(f"daily: {daily_lunch+daily_groceries}")
print(f"weekly: {(daily_groceries+daily_lunch)*7}")
print(f"monthly: {(daily_lunch+daily_groceries)*30}")