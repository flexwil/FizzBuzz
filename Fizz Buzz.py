# pc spielt alleine
def pc_vs_pc(rounds, f, b):
    for i in range(1, rounds + 1):
        if i % f == 0 and i % b == 0:
            print('FizzBuzz')
        elif i % f == 0:
            print('Fizz')
        elif i % b == 0:
            print('Buzz')
        else:
            print(i)

# Main Function für Spiel Mensch ggn PC
def user_vs_pc(number, player_score, f, b):
    while True:
        number += 1
        input_pc(number, f, b)
        number += 1
        player_score += 1
        if not input_check(input_user(), number, f, b):
            player_name = input(f'Verloren!!! Dein Score ist: {player_score}! \n Gib deinen Namen ein: ')
            save_score(player_name, player_score)
            break

# PC Ausgabe Berechnung
def input_pc(number, f, b):
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

def save_score(player_name, player_score):
    writescore = player_name + '...' + str(player_score) + '\n'
    myhighscore = open(highscore, 'a')
    myhighscore.write(writescore)
    myhighscore.close()

def show_score():
    myhighscore = open(highscore, 'r')
    print(myhighscore.read())
    myhighscore.close()

def select_numbers():
    f = int(input('Welche Zahl ist Fizz?: '))
    b = int(input('Welche Zahl ist Buzz?: '))
    return f, b

def main():
    opp = input('Drücke 1 wenn du gegen den PC spielen möchtest, 2 für die Highscore, ansonsten klicke einfach weiter...')
    if opp == '1':
        f, b = select_numbers()
        user_vs_pc(number, player_score, f, b)
    elif opp == '2':
        show_score()
        main()
    else:
        rounds = int(input('Bis zu welcher Zahl soll gespielt werden?: '))
        f, b = select_numbers()
        pc_vs_pc(rounds, f, b)

number = 0
player_score = -1
highscore = 'highscore.txt'


main()