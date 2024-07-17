
def pc_vs_pc():
    for i in range(1, rounds):
        if i % f == 0 and i % b == 0:
            print('FizzBuzz')
        elif i % f == 0:
            print('Fizz')
        elif i % b == 0:
            print('Buzz')
        else:
            print(i)

def user_vs_pc(number):
    while True:
        number += 1
        input_pc()
        number += 1
        input_user()
        if input_check(user, number, f, b):
            print('lost')
            break

def input_pc():
    if number % f == 0 and number % b == 0:
        print('FizzBuzz')
    elif number % f == 0:
        print('Fizz')
    elif number % b == 0:
        print('Buzz')
    else:
        print(number)
    return number

def input_user():
    user = input('Du bist dran: ')
    return user

def input_check(user, number, f, b):
    if number % f == 0 and number % b == 0 and user != 'FizzBuzz':
        return True
    elif number % f == 0 and user != 'Fizz':
        return True
    elif number % b == 0 and user != 'Buzz':
        return True
    elif number == int(user):
        return True
    else:
        return False

number = 0
f = int(input('Welche Zahl ist Fizz?: '))
b = int(input('Welche Zahl ist Buzz?: '))
opp = input('Drücke 1 wenn du gegen den PC spielen möchtest, ansonsten klicke einfach weiter...')

if opp == '1':
    user_vs_pc(number)
else:
    rounds = int(input('Bis zu welcher Zahl soll gespielt werden?: ')) + 1
    pc_vs_pc()

