fahrenheit=int(input("Please type in a temperature (F):" ))
celsius=(fahrenheit-32)/1.8
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")

print("")

hourly_wage=float(input("hourly wage?"))
hour_worked=int(input("hours worked?"))
day_of_week=input("day of the week?")
if day_of_week == "Sunday" :
    print(f"{(hourly_wage*hour_worked)*2}")
else:
    print(f"{(hourly_wage*hourly_wage)}")

print("")

age=int(input("How old are you?"))
if age >= 44:
    print("You are too old for this sh*t")
elif age >= 18 :
    print("Here is Dark Souls. Lol")
elif age < 18 :
    print("You can't play Dark Souls")

print("")

num1=int(input("Please enter a first number"))
num2=int(input("Please enter a second number"))
if num1>num2 :
    print(f"First one is greater ({num1} > {num2})")
elif num2>num1:
    print(f"Second one is greater {num2} > {num1}")
else:
    print(f"These are equal {num1} = {num2}")

print("")

game1=input("Please enter a game name?")
game2= input("Please enter a game name too?")
if game1 > game2 :
    print(f"{game2} comes alphabetically last")
elif game2 > game1 :
    print(f"{game1} comes alphabetically last")
else:
    print("These are same!")

print("")

community=input("Which community do you belong to?")
if community == "NCR" or community == "New California Republic" or community == "Brotherhood of Steel" or community == "Caesar's Legion" or community == "Graet Khans" or community == "Vault Dweller" :
    print("You're belong to Fallout Universe.")
else:
    print("Nope, you are not belong to Fallout Lore")

print("")

point=int(input("What is your exam point?"))
if point < 0 :
    print("You what?")
elif point <= 49 :
    print("fail")
elif point <= 59 :
    print("1")
elif point <= 69 :
    print("2")
elif point <= 79 :
    print("3")
elif point <= 89 :
    print("4")
elif point <= 100 :
    print("5")
else:
    print("impossible!")

print("")

number=int(input("Please type in a number:"))
if number % 3 and number % 5 :
    print("FizzBuzz")
elif number % 3 :
    print("Fizz")
elif number % 5 :
    print("Buzz")
number1=int(input("Please type in a number: "))
if number1 > 0 and number1 % 2 == 0 :
    print("The number is even")
elif number1 % 2 != 0 and  number1 > 0 :
    print("The number is odd")
else:
    print("The number is negative or zero")

print("")

year=int(input("Please type in a year?"))
if year % 400 == 0 :
    print("That year is a leap year.")
elif year % 100 == 0 :
    print("This year is a leap year.")
elif year % 4 == 0 :
    print("This year is a leap year.")
else:
    print("That year is not a leap year.")


