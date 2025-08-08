import random
from words import word_list
from hangman_art import stages, logo
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def play_hangman():
    lives = 6
    print(Fore.CYAN + logo)

    chosen_word = random.choice(word_list)
    placeholder = "_" * len(chosen_word)
    print(Fore.YELLOW + "Word to guess: " + placeholder)

    chosen_letters = []
    game_over = False

    while not game_over:
        print(Fore.MAGENTA + f"\n******************** {lives}/6 LIVES LEFT ********************")
        guess = input(Fore.WHITE + "Guess a letter: ").lower()

        if guess in chosen_letters:
            print(Fore.LIGHTBLACK_EX + f"You've already guessed '{guess}'. Try another letter.")
            continue
        else:
            chosen_letters.append(guess)

        display = ""
        for letter in chosen_word:
            if letter in chosen_letters:
                display += letter
            else:
                display += "_"

        print(Fore.YELLOW + "Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print(Fore.RED + f"You guessed '{guess}', that's not in the word. You lose a life.")
            if lives == 0:
                print(Fore.RED + "\n******************** YOU LOSE! ********************")
                print(Fore.RED + f"The word was: {chosen_word}")
                game_over = True

        if "_" not in display:
            print(Fore.GREEN + "\n******************** YOU WIN! ********************")
            print(Fore.GREEN + f"The word was: {chosen_word}")
            game_over = True

        print(Fore.BLUE + stages[6 - lives])

if __name__ == "__main__":
    play_hangman()
