#task40
cityname=input("please enter a city name: ")
repetition=int(input("please enter a repetition: "))
word= "li"
print(f"{cityname}{word * repetition}lerle")

#task41
argument1=input("Please enter first name: ")
argument2=input("Please enter second name: ")
def longer_string(argument1, argument2):
    len1= len(argument1)
    len2= len(argument2)
    if len1 > len2 :
        print(argument1)
    elif len2 > len1 :
        print(argument2)
    else:
        print("Their length are same")
longer_string(argument1,argument2)

#task42
def user_string():
    your_input=input("Your input: ")
    print(f"*{your_input}*")
user_string()

#task43 
def user_input():
    your_input1=input("Your input: ")
    lenght=len(your_input1)
    print(your_input1)
    print(lenght* "-")
user_input()

#task44
def user_string1():
    your_input2= input("Your Input: ")
    max1= 18 - len(your_input2)
    left= max1 // 2
    right= max1 - left
    print("-" * 20)
    print("|" + ">" * left + your_input2 + "<" * right + "|")
    print("-" * 20)
user_string1()

#task45
def takes3_input():
    string1=input("Please enter string: ")
    integer1=int(input("Please first integer: "))
    integer2=int(input("Please last integer: "))
    print(string1 [integer1:integer2])
takes3_input()

#task46
def takes2_input():
    user_s=input("Please enter string: ")
    user_i=int(input("Please enter integer: "))
    print(user_s [0:user_i])
takes2_input()

#task47
def takes2.1_input():
    user_s=input("Please enter string: ")
    user_i=int(input("Please enter integer: "))
    print(user_s [user_i:0])
takes2.1_input()
 
#task48
def search1():
    user_i1=input("Please enter string: ")
    if "a" in user_i1:
        print("found")
    else:
        print("not found")
search1()

#task49
def search2():
    user_i2=input("Please enter string: ")
    user_i3=input("Please enter search item: ")
    if user_i3 in user_i2:
        print("found")
    else:
        print("not found")
search2()

#task50
def search3():
    user_i4=input("Please enter string: ")
    user_i5=input("Please enter search item: ")
    if user_i5 in user_i4:
        print(f"found it at {user_i4.find(user_i5)}")
    else:
        print("not found")
search3()

#task51
def search_sentence():
    sentence = "The quick brown fox jumps over the lazy dog"
    my_flag = True

    while my_flag:
        user_input1 = input("What are you looking for? ")

        if user_input1 == "-1":
            print("Bye.")
            my_flag = False
        else:  
            index = sentence.find(user_input1)

            if index != -1:
                print(f"found it at {index}")
            else:
                print("not found")
search_sentence()


