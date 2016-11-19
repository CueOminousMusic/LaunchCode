from helpers import alphabet_position, rotate_character



def encrypt_vig(text, key):
    output = ""
    key_index = 0
    for char in text:
        rot = alphabet_position(key[key_index%len(key)])
        output = output + rotate_character(char, rot)
        if char in string.ascii_letters:
            key_index += 1
    return output


text = input("Your message?")
key = input("Your encryption key?")
print(encrypt_vig(text, key))