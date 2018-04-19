import random
import os
import sys


def load_data(filename):
    try:
        with open(filename, "r") as f:
            lines = f.read().splitlines()
            return random.choice(lines)
    except IOError:
        print("Couldn't open file")
        exit(1)


def print_game(guessed_string, lives, tried_chars):
    os.system('clear')
    print(" ".join(guessed_string))
    print("Chances left: ", lives)
    print("You tried this letters: ", ", ".join(tried_chars))


def find_indexes(a, secret):
    indexes = list()
    for i, char in enumerate(secret):
        if char == a:
            indexes.append(i)
    return indexes


def game(filename):
    secret = load_data(filename)
    lives = 5
    tried_chars = set()
    guessed_string = "_" * len(secret)
    while True:
        if guessed_string == secret:
            print(secret)
            print("You won !")
            return
        if lives == 0:
            print(secret)
            print("You lost!")
            return
        print_game(guessed_string, lives, sorted(tried_chars))
        a = input("Give me a letter ")
        if len(a) == 0:
            continue
        a = a[0]
        if a in tried_chars:
            continue
        tried_chars.add(a)
        if a in secret:
            indexes = find_indexes(a, secret)
            for i in indexes:
                guessed_string = guessed_string[:i] + a + guessed_string[i + 1:]
        else:
            lives -= 1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You should provide one argument")
        exit(1)
    game(sys.argv[1])
