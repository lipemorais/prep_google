# https://www.beecrowd.com.br/judge/pt/problems/view/1068

def satisfy_beecrowd():
    while True:
        try:
            line = input()
            result = parentheses_balance(line)
            print(result)
        except EOFError:
            break


def parentheses_balance(line):
    counter = 0

    for letter in line:
        if letter == "(":
            counter = counter + 1
        elif letter == ")":
            counter = counter - 1

        if counter < 0:
            break

    if counter == 0:
        return "correct"

    return "incorrect"

satisfy_beecrowd()
