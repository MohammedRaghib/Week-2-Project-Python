import random
import tkinter as tk
from tkinter import messagebox

word_list = ["Coding", "Variable", "Function", "Module", "Import", "Loop", "List", "Dictionary", "Tuple", "String", "Integer", "Boolean", "Class", "Object", "Syntax", "Indentation", "Library", "Decorator", "Parameter", "Argument"]
chosen_word = ''
displayed_word = []
guessed_letters_tracker = []
incorrect_guesses_remaining = 6

def start_new_game():
    global chosen_word, displayed_word, guessed_letters_tracker, incorrect_guesses_remaining

    chosen_word = random.choice(word_list).lower()
    displayed_word = ["_"] * len(chosen_word)
    guessed_letters_tracker = []
    incorrect_guesses_remaining = 6

    word_display_label.config(text=" ".join(displayed_word))
    remaining_guesses_label.config(text=f'Tries left: {incorrect_guesses_remaining}')
    letter_entry_field.delete(0, tk.END)
    guess_action_button.config(state=tk.NORMAL)
    guessed_letters_label.config(text="Guessed letters: ")

def process_guess():
    global incorrect_guesses_remaining

    current_guess = letter_entry_field.get().lower()
    letter_entry_field.delete(0, tk.END)

    if not current_guess.isalpha() or len(current_guess) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if current_guess in guessed_letters_tracker:
        messagebox.showinfo("Already Guessed", f"You've already guessed '{current_guess}'. Try another letter.")
        return

    guessed_letters_tracker.append(current_guess)
    guessed_letters_label.config(text="Guessed letters: " + ", ".join(sorted(guessed_letters_tracker)))

    if current_guess in chosen_word:
        for index, character in enumerate(chosen_word):
            if character == current_guess:
                displayed_word[index] = current_guess
        word_display_label.config(text=" ".join(displayed_word))

        if "_" not in displayed_word:
            messagebox.showinfo("Hangman", "Congratulations! You guessed the word!")
            guess_action_button.config(state=tk.DISABLED)
    else:
        incorrect_guesses_remaining -= 1
        remaining_guesses_label.config(text=f'Tries left: {incorrect_guesses_remaining}')
        if incorrect_guesses_remaining == 0:
            messagebox.showinfo("Hangman", f"Game Over! The word was '{chosen_word}'.")
            guess_action_button.config(state=tk.DISABLED)

main_window = tk.Tk()
main_window.title('Hangman')
main_window.geometry('500x500')
main_window.resizable(False, False)

game_frame = tk.Frame(main_window, padx=20, pady=20)
game_frame.pack(expand=True, fill=tk.BOTH)

tk.Label(game_frame, text='Guess the word!', font=('Arial', 18, 'bold')).pack(pady=10)

word_display_label = tk.Label(game_frame, text='', font=('Courier New', 24, 'bold'))
word_display_label.pack(pady=20)

remaining_guesses_label = tk.Label(game_frame, text=f'Tries left: {incorrect_guesses_remaining}', font=('Arial', 14))
remaining_guesses_label.pack(pady=5)

guessed_letters_label = tk.Label(game_frame, text='Guessed letters: ', font=('Arial', 12))
guessed_letters_label.pack(pady=5)

tk.Label(game_frame, text='Enter your guess: ', font=('Arial', 12)).pack(pady=5)
letter_entry_field = tk.Entry(game_frame, width=10, font=('Arial', 16))
letter_entry_field.pack(pady=5)
letter_entry_field.bind("<Return>", lambda event=None: process_guess())

guess_action_button = tk.Button(game_frame, text='Try Guess', command=process_guess, font=('Arial', 14), bg='lightgreen', fg='black')
guess_action_button.pack(pady=10)

start_new_game_button = tk.Button(game_frame, text='New Game', command=start_new_game, font=('Arial', 14), bg='lightblue', fg='black')
start_new_game_button.pack(pady=10)

start_new_game()

main_window.mainloop()