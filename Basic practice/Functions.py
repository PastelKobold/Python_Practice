#Writing functions in Python

def print_phrase():
    print("Hello!")
def print_2():
    print("How are you?")

x = 0

User_input = 0
User_input = input("Which function?: ")
x = int(User_input)

if x == 1:
    print_phrase()
if x == 2:
    print_2()

