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
    
    
def game_control(language):
    word = retrieve_word(language).upper()
    masked_word = mask(word)
    life = 8
    print(word)

    while True:
        if life > 0:
            print_ui(game_ui=True, masked_word=masked_word, life=life, word=word)
            user_input = input("Please enter a letter or try to guess!\n").upper()

            if len(user_input) > 1:
                if is_true(word, user_input):
                    print_ui(win=True)
                    return game_control(language)
            elif len(user_input) == 1: #eğer haf tahmini ise
                if is_letter_there(word, user_input):
                    masked_word = update_masked_word(word, masked_word, user_input)
                    continue
                else:
                    life -= 1
                    print("Sorry... your have lost 1 life point.")
                    continue
            else:
                print("Your input is invalid.")
        else:
            print_ui(game_ui=True, masked_word=masked_word, life=life, word=word, lost=True)
            break
    return game_control(language)
    

def print_ui(word=None, masked_word=None, life=None, win=False, lost=False, game_ui=False):
    if game_ui:
        human = {
            0: """
  ________
 |       |
⚪       |
 |       |
/|\      |
 |       |
/ \      |
       __|__
            """,
            1: """
  ________
 |       |
⚪       |
 |       |
 |\      |
 |       |
/ \      |
       __|__
            """,
            2: """
  ________
 |       |
⚪       |
 |       |
 |       |
 |       |
/ \      |
       __|__
            """,
            3: """
  ________
 |       |
⚪       |
 |       |
 |       |
 |       |
  \      |
       __|__
            """,
            4: """
  ________
 |       |
⚪       |
 |       |
 |       |
 |       |
         |
       __|__
            """,
            5: """
  ________
 |       |
⚪       |
         |
         |
         |
         |
       __|__
            """,
            6: """
  ________
 |       |
         |
         |
         |
         |
         |
       __|__
            """,
            7: """
         |
         |
         |
         |
         |
         |
       __|__
            """,
            8: """
        
       
     
       
      
       
     
       __|__
            """,
        }
        
        print(human[life], "\n", list_to_string(masked_word))
    if win: #win parameter
        os.system("cls") #for Windows
        print("Congratulations! You guessed the word!")
    if lost: #word & lost parameters
        print("Sorry, you are out of lives! The word was:\n{}".format(word))
        

def menu():
    language = input("Please type in the language you want to play with.")
    game_control(language)

    print(mask(language))


menu()
