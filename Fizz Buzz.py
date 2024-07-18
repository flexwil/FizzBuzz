# pc spielt alleine
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

# Main Function für Spiel Mensch ggn PC
def user_vs_pc(number):
    while True:
        number += 1
        input_pc(number)
        number += 1
        if not input_check(input_user(), number, f, b):
            print('lost')
            break

# PC Ausgabe Berechnung
def input_pc(number):
    if number % f == 0 and number % b == 0:
        print('FizzBuzz')
    elif number % f == 0:
        print('Fizz')
    elif number % b == 0:
        print('Buzz')
    else:
        print(number)
    return number

# Eingabe Nutzer
def input_user():
    user = input('Du bist dran: ')
    return user

# Überprüfung Eingabe
def input_check(user, number, f, b):
    if number % f == 0 and number % b == 0:
        return user == 'FizzBuzz'
    elif number % f == 0:
        return user == 'Fizz'
    elif number % b == 0:
        return user == 'Buzz'
    else:
        return number == int(user)



number = 0

f = int(input('Welche Zahl ist Fizz?: '))
b = int(input('Welche Zahl ist Buzz?: '))
opp = input('Drücke 1 wenn du gegen den PC spielen möchtest, ansonsten klicke einfach weiter...')

if opp == '1':
    user_vs_pc(number)
else:
    rounds = int(input('Bis zu welcher Zahl soll gespielt werden?: ')) + 1
    pc_vs_pc()

