#Comment
User_input = 0
User_input = input('x = ?: ')
x = int(User_input)
print('x =', x)
while x < 25:
    if x < 10:
        print('x is smaller than 10!')
    if x > 10 and x < 20 :
        print('x is between 10 and 20!')
    if x > 20:
        print('x is greater than 20!')
    x = x + 1

print('All done!')
