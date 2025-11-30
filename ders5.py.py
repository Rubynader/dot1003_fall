#task53
def spruce():
    height = int(input("Spruce height: "))
    box = int(input("Box size: "))
    print("-" * box)
    print("|" + " " * (box - 2) + "|")
    for i in range(height):
        stars = "*" * (2 * i + 1)
        line =stars 
        spaces_needed = (box - 2) - len(line)
        line_spaces = line + " " * spaces_needed 
        print("|" + line_spaces + "|")
    trunk = "*"
    spaces= (box - 2) - len(trunk)
    trunk_line = trunk + " " * spaces
    print("|" + trunk_line + "|")
    print("-" * box)

spruce()
    
#task54
def search_sentence():
    sentence = "The quick brown fox jumps over the lazy dog"
    my_flag=True
    while my_flag:
        item = input("Which item do you want to search? ")
        if item == "":
            print("Empty input, exiting.")
            my_flag=False
        count = sentence.count(item)
        print(f"item {item} appeared {count} times")

search_sentence()

#task55
def search_item():
    user_input = input("Enter the input to search: ")
    item = input("Which item do you want to search?: ")
    count = user_input.count(item)
    print(f"item {item} appeared {count} times")

search_item()

#task56
def clear_vowels(st):
    vowels = "aeıioöuüAEIİOÖUÜ"
    result = ""
    for ch in st:
        if ch not in vowels:
            result += ch
    return result
menu_button = "new game"
print(clear_vowels(menu_button))
my_flag=True
while True:
    text = input("Enter a string (or 'exit' to quit): ")
    if text == "exit" or text == "Exit" or text == "EXIT":
        my_flag=False
    print(clear_vowels(text))

#task57
