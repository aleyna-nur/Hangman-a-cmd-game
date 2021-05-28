import random
import string
import os
#TODO: Girilen harfleri ekrana yazdır.

letters = list(string.ascii_uppercase)
letters.append("Ç")
letters.append("Ğ")
letters.append("Ü")

def retrieve_word(language):
    global letters
    random.shuffle(letters)
    letter = letters[0]
    
    try:
        path = "{lng}-database/{ltr}.txt".format(lng=language, ltr=letter)
        with open(path, "r", encoding="utf-8") as file:
            return random.choice(file.readlines()).strip("\n")
    except:
        return retrieve_word(language)


def list_to_string(the_list):
    string_to_be_printed = ""
    for char in the_list:
        string_to_be_printed += char
    return string_to_be_printed


def mask(word):
    masked_word = []
    for char in word:
        if char == " ":
            masked_word.append(" ")
        else:
            masked_word.append("_ ")
    return masked_word


def update_masked_word(word, masked_word, user_input):
    #Sorulan kelimede [ŞU HARF VAR MI] sorusunun cevabını verecek olan fonksiyon.
    index = -1
    for char in word:
        index += 1
        if char == user_input:
            masked_word.pop(index)
            masked_word.insert(index, user_input)
    return masked_word


def is_letter_there(word, user_input):
    if user_input in word:
        return True
    else:
        return False


def is_true(word, user_input):
    if user_input == word:
        return True
