from tkinter import *
from PIL import ImageTk, Image
from words import words_EN
import random, dutch_words, string, os, sys

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    global language
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    if language.get() == 'English':
        lives = 10

        word = get_valid_word(words_EN)
        word_letters = set(word)

        while len(word_letters) > 0 and lives > 0:

            text_lives = Label(root, text=f'You have {lives} lives. ', bg=BG_COLOR, fg=FG_COLOR)
            text_lives.place(x = 1, y = 1)

            used_letters_text = Label(root, text='Used letters:', bg=BG_COLOR, fg=FG_COLOR)
            used_letters_label = Label(root, text=(', '.join(used_letters)), bg=BG_COLOR, fg=FG_COLOR)
            used_letters_text.place(x = 1, y = 60)
            used_letters_label.place(x = 1, y = 80)

            letter_list = [letter if letter in used_letters else '-' for letter in word]

            crnt_word = Label(root, text=('Current word: ' + ' '.join(letter_list) + '  '), bg=BG_COLOR, fg=FG_COLOR)
            crnt_word.place(x = 130, y = 1)

            enter.wait_variable(enter_press)

            user_letter = user_guess.get().upper()
            user_guess.delete(0, END)

            while user_letter == '':
                log4 = Label(root, text='You need to put in a letter.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                log4.place(x=130, y=60)
                user_guess.delete(0, END)
                enter.wait_variable(enter_press)
                user_letter = user_guess.get().upper()
            
            user_guess.delete(0, END)

            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)

                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    log4 = Label(root, text='Good guess!\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                    log4.place(x=130, y=60)

                else:
                    lives -= 1
                    log2 = Label(root, text='The word does not contain this letter.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                    log2.place(x=130, y=60)

            elif user_letter in used_letters:
                log2 = Label(root, text='You have already used that letter, guess again.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                log2.place(x=130, y=60)

            else:
                log2 = Label(root, text='You didn\'t type in a valid character, guess again.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                log2.place(x=130, y=60)
            
            used_letters_text = Label(root, text='Used letters:  ', bg=BG_COLOR, fg=FG_COLOR)
            used_letters_label = Label(root, text=(', '.join(used_letters)), bg=BG_COLOR, fg=FG_COLOR)
            used_letters_text.place(x = 1, y = 60)
            used_letters_label.place(x = 1, y = 80)

        letter_list = [letter if letter in used_letters else '-' for letter in word]
        crnt_word = Label(root, text=('Current word: ' + ' '.join(letter_list) + '  '), bg=BG_COLOR, fg=FG_COLOR)
        crnt_word.place(x = 130, y = 1)
        if lives > 0:
            user_guess.delete(0, END)
            win_text_1 = Label(root, text='You guessed the word! Press enter to play again.', bg=BG_COLOR, fg=FG_COLOR)
            win_text_2 = Label(root, text=('The word: ' + ''.join(word)), bg=BG_COLOR, fg=FG_COLOR)
            win_text_1.place(x = 1, y = 105)
            win_text_2.place(x = 1, y = 130)
            quit_button = Button(root, text='Quit', highlightbackground=BG_COLOR, fg='#000000', command=lambda:sys.exit()) # For background color button, use highlightbackground
            quit_button.place(x = 475, y = 200)
            enter.wait_variable(enter_press)
            reset()

        else:
            user_guess.delete(0, END)
            win_text_1 = Label(root, text='You failed. Press enter to play again.', bg=BG_COLOR, fg=FG_COLOR)
            win_text_2 = Label(root, text=('The word was: ' + ''.join(word)), bg=BG_COLOR, fg=FG_COLOR)
            win_text_1.place(x = 1, y = 105)
            win_text_2.place(x = 1, y = 130)
            quit_button = Button(root, text='Quit', highlightbackground=BG_COLOR, fg='#000000', command=lambda:sys.exit()) # For background color button, use highlightbackground
            quit_button.place(x = 475, y = 200)
            enter.wait_variable(enter_press)
            reset()

    elif language.get() == 'Nederlands':
        label = Label(root, text='Raad een letter:', bg=BG_COLOR, fg=FG_COLOR)
        label.place(x = 1, y = 25)
        lives = 10

        word = get_valid_word(words_NL)
        word_letters = set(word)

        while len(word_letters) > 0 and lives > 0:
            text_lives = Label(root, text=f'Je hebt {lives} levens.  ', bg=BG_COLOR, fg=FG_COLOR)
            text_lives.place(x = 1, y = 1)

            used_letters_text = Label(root, text='Gebruikte letters:', bg=BG_COLOR, fg=FG_COLOR)
            used_letters_label = Label(root, text=(', '.join(used_letters)), bg=BG_COLOR, fg=FG_COLOR)
            used_letters_text.place(x = 1, y = 60)
            used_letters_label.place(x = 1, y = 80)

            letter_list = [letter if letter in used_letters else '-' for letter in word]

            crnt_word = Label(root, text=('Huidige woord: ' + ' '.join(letter_list) + '  '), bg=BG_COLOR, fg=FG_COLOR)
            crnt_word.place(x = 130, y = 1)

            enter.wait_variable(enter_press)

            user_letter = user_guess.get().upper()
            user_guess.delete(0, END)

            while user_letter == '':
                user_guess.delete(0, END)
                log4 = Label(root, text='Je moet een letter typen.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                log4.place(x=130, y=60)
                enter.wait_variable(enter_press)
                user_letter = user_guess.get().upper()

            user_guess.delete(0, END)

            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)

                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    log4 = Label(root, text='Goed geraden!\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                    log4.place(x=130, y=60)

                else:
                    lives -= 1
                    log2 = Label(root, text='Deze letter zit niet in het woord.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                    log2.place(x=130, y=60)

            elif user_letter in used_letters:
                log2 = Label(root, text='Deze letter heb je al geraden, raad nog een keer.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                log2.place(x=130, y=60)

            else:
                log2 = Label(root, text='Je hebt geen geldig karakter ingevoerd, raad nog een keer.\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
                log2.place(x=130, y=60)
            
            used_letters_text = Label(root, text='Gebruikte letters:  ', bg=BG_COLOR, fg=FG_COLOR)
            used_letters_label = Label(root, text=(', '.join(used_letters)), bg=BG_COLOR, fg=FG_COLOR)
            used_letters_text.place(x = 1, y = 60)
            used_letters_label.place(x = 1, y = 80)

        letter_list = [letter if letter in used_letters else '-' for letter in word]
        crnt_word = Label(root, text=('Huidige woord: ' + ' '.join(letter_list) + '  '), bg=BG_COLOR, fg=FG_COLOR)
        crnt_word.place(x = 130, y = 1)
        if lives > 0:
            user_guess.delete(0, END)
            win_text_1 = Label(root, text='Je hebt het woord geraden! Druk op enter om nog een keer te spelen.', bg=BG_COLOR, fg=FG_COLOR)
            win_text_2 = Label(root, text=('Het woord: ' + ''.join(word)), bg=BG_COLOR, fg=FG_COLOR)
            win_text_1.place(x = 1, y = 105)
            win_text_2.place(x = 1, y = 130)
            quit_button = Button(root, text='Quit', highlightbackground=BG_COLOR, fg='#000000', command=lambda:sys.exit()) # For background color button, use highlightbackground
            quit_button.place(x = 475, y = 200)
            enter.wait_variable(enter_press)
            reset()

        else:
            user_guess.delete(0, END)
            win_text_1 = Label(root, text='Je bent af. Druk op enter om nog een keer te spelen.', bg=BG_COLOR, fg=FG_COLOR)
            win_text_2 = Label(root, text=('The word was: ' + ''.join(word)), bg=BG_COLOR, fg=FG_COLOR)
            win_text_1.place(x = 1, y = 105)
            win_text_2.place(x = 1, y = 130)
            quit_button = Button(root, text='Quit', highlightbackground=BG_COLOR, fg='#000000', command=lambda:sys.exit()) # For background color button, use highlightbackground
            quit_button.place(x = 475, y = 200)
            enter.wait_variable(enter_press)
            reset()

BG_COLOR = '#393630'
FG_COLOR = '#ffffff'

root = Tk()
root.geometry('525x230')
root.title('Hangman')
root.configure(bg=BG_COLOR)
root.resizable(False, False)

def quitexit():
    sys.exit()

def func(event):
    enter_press.set(1)
root.bind('<Return>', func)

words_NL = dutch_words.get_ranked()

user_guess = Entry(root, bg=BG_COLOR, fg=FG_COLOR)
enter_press = IntVar()
enter = Button(root, text='Submit guess', bg=BG_COLOR, fg=FG_COLOR, command=lambda: enter_press.set(1))
user_letter = ''
text_lives = Label(root, text='Choose language', bg=BG_COLOR, fg=FG_COLOR)
crnt_word = Label(root, text='Kies een taal', bg=BG_COLOR, fg=FG_COLOR)
label = Label(root, text='Guess letter:', bg=BG_COLOR, fg=FG_COLOR)
used_letters_text = Label(root, text='Used letters:', bg=BG_COLOR, fg=FG_COLOR)
used_letters_label = Label(root, text='\t\t\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
quit_button = Button(root, text='Quit', highlightbackground=BG_COLOR, fg='#000000', command=lambda:sys.exit()) # For background color button, use highlightbackground

languages = ['English', 'Nederlands']
language = StringVar(root)
language.set('Choose language')
language_choices = OptionMenu(root, language, *languages)
language_choices.config(bg=BG_COLOR)

log2 = Label(root, text='', bg=BG_COLOR, fg=FG_COLOR)

crnt_word_cover = Label(root, text='\t\t            ', bg=BG_COLOR, fg=FG_COLOR)

def callback(*args):
    print('working')
    hangman()
language.trace("w", callback)

text_lives.place(x = 1, y = 1)
crnt_word.place(x = 130, y = 1)
language_choices.place(x = 325, y = 27)

label.place(x = 1, y = 25)
user_guess.place(x = 130, y = 25)

used_letters_text.place(x = 1, y = 60)
used_letters_label.place(x = 1, y = 80)

log2.place(x = 130, y = 60)

quit_button.place(x = 475, y = 200)

def reset():
    global user_guess, enter_press, user_letter, text_lives, crnt_word, label, used_letters_text,\
    used_letters_label, languages, language, language_choices, log2, crnt_word_cover, quit_button
    for widgets in root.winfo_children():
        widgets.destroy()

    user_guess = Entry(root, bg=BG_COLOR, fg=FG_COLOR)
    enter_press = IntVar()
    enter = Button(root, text='Submit guess', bg=BG_COLOR, fg=FG_COLOR, command=lambda: enter_press.set(1))
    user_letter = ''
    text_lives = Label(root, text='Choose language', bg=BG_COLOR, fg=FG_COLOR)
    crnt_word = Label(root, text='Kies een taal', bg=BG_COLOR, fg=FG_COLOR)
    label = Label(root, text='Guess letter:', bg=BG_COLOR, fg=FG_COLOR)
    used_letters_text = Label(root, text='Used letters:', bg=BG_COLOR, fg=FG_COLOR)
    used_letters_label = Label(root, text='\t\t\t\t\t', bg=BG_COLOR, fg=FG_COLOR)
    quit_button = Button(root, text='Quit', highlightbackground=BG_COLOR, fg='#000000', command=lambda:sys.exit()) # For background color button, use highlightbackground

    languages = ['English', 'Nederlands']
    language = StringVar(root)
    language.set('Choose language')
    language_choices = OptionMenu(root, language, *languages)
    language_choices.config(bg=BG_COLOR)

    log2 = Label(root, text='\t\t\t\t\t', bg=BG_COLOR, fg=FG_COLOR)

    crnt_word_cover = Label(root, text='\t\t            ', bg=BG_COLOR, fg=FG_COLOR)

    def callback(*args):
        print('working')
        hangman()
    language.trace("w", callback)

    text_lives.place(x = 1, y = 1)
    crnt_word.place(x = 130, y = 1)
    language_choices.place(x = 325, y = 27)

    label.place(x = 1, y = 25)
    user_guess.place(x = 130, y = 25)

    used_letters_text.place(x = 1, y = 60)
    used_letters_label.place(x = 1, y = 80)

    log2.place(x = 130, y = 60)

    quit_button.place(x = 475, y = 200)

root.mainloop()