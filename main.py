import random

alph_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alph_upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_str = []
for x in numbers:
    numbers_str.append(str(x))
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']
breaks = [' ']
mix_chars = alph_low + alph_upp + numbers_str + symbols + breaks
mix_chars_str = ''
for x in mix_chars:
    mix_chars_str += str(x)

class EncryptDecryptError:
    class InvalidKey(Exception):
        pass
    class UnsupportedCharacter(Exception):
        pass

class settings:
    global alph_low, alph_upp, numbers, symbols, breaks, mix_chars, mix_chars_str
    def refresh_configurations(self):
        global alph_low, alph_upp, numbers, symbols, breaks, mix_chars, mix_chars_str
        mix_chars = alph_low + alph_upp + numbers_str + symbols + breaks
        mix_chars_str = ''
        for x in mix_chars:
            mix_chars_str += str(x)
    def __init__(self):
        self.refresh_configurations()
    def support_line_break(support:bool):
        global alph_low, alph_upp, numbers, symbols, breaks, mix_chars, mix_chars_str
        if support:
            breaks = [' ', '\n']
        elif not support:
            breaks = [' ']
        settings.refresh_configurations(settings)

def create_key():
    global mix_chars
    mix_chars_left = []
    for x in mix_chars:
        mix_chars_left.append(x)
    key = ''
    for x in range(len(mix_chars)):
        char = random.choice(mix_chars_left)
        key += str(char)
        mix_chars_left.remove(char)
    return key

def key_is_valid(key:str):
    global mix_chars
    used_chars = ''
    if not type(key) == str:
        return False
    if not len(str(key)) == len(mix_chars):
        return False
    for x in str(key):
        if not x in used_chars:
            used_chars += str(x)
        else:
            return False
    return True

def encrypt(string:str, key:str):
    global mix_chars, mix_chars_str
    if not key_is_valid(str(key)):
        raise EncryptDecryptError.InvalidKey('key is invalid')
    encrypted = ''
    line_counter = 1
    character_counter = 0
    for x in range(len(str(string))):
        if str(string)[x] == '\n':
            character_counter = 0
            line_counter += 1
        else:
            character_counter += 1
        if str(string)[x] not in mix_chars:
            if str(string)[x] == '\n':
                raise EncryptDecryptError.UnsupportedCharacter(f'Unsupported character in string (enter / line break) Ln: {line_counter} Col: {character_counter}')
            raise EncryptDecryptError.UnsupportedCharacter(f'Unsupported character in string ({string[x]}) Ln: {line_counter} Col: {character_counter}')
        for x_in_key in range(len(str(key))):
            if str(key)[x_in_key] == str(string)[x]:
                break
        encrypted += str(mix_chars[x_in_key])
    return encrypted

def decrypt(string:str, key:str):
    global mix_chars, mix_chars_str
    if not key_is_valid(str(key)):
        raise EncryptDecryptError.InvalidKey('key is invalid')
    decrypted = ''
    line_counter = 1
    character_counter = 0
    for x in range(len(str(string))):
        if str(string)[x] == '\n':
            character_counter = 0
            line_counter += 1
        else:
            character_counter += 1
        if str(string)[x] not in mix_chars:
            if str(string)[x] == '\n':
                raise EncryptDecryptError.UnsupportedCharacter(f'Unsupported character in string (enter / line break) Ln: {line_counter} Col: {character_counter}')
            raise EncryptDecryptError.UnsupportedCharacter(f'Unsupported character in string ({string[x]}) Ln: {line_counter} Col: {character_counter}')
        for x_in_mix in range(len(mix_chars)):
            if str(mix_chars[x_in_mix]) == str(string)[x]:
                '''print(mix_chars[x_in_mix] + ' == ' + str(string)[x])''' # just for testing
                break
        decrypted += str(key[x_in_mix])
    return decrypted
