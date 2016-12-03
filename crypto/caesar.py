from helpers import alphabet_position, rotate_character
from sys import argv, exit


def encrypt(text, rot):
    output = ""
    for char in text:
        output = output+rotate_character(char, rot)
    return output


def user_input_is_valid(cl_args):
    if len(cl_args) == 2:
        if cl_args[1].isdigit():
            return True
    return False


def main():
    if user_input_is_valid(argv):
        text = input("Enter your message:")
        rot = int(argv[1])
        print(encrypt(text,rot))
    else:
        print("usage: python3 caesar.py n")
        exit()


if __name__ == '__main__':
    main()
