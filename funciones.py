import random

def play_chipiado():
    seguir_jugando = True
    print("Hello user. Welcome to the game selector.")
    while seguir_jugando == True:
        seleccion = input("¿Which game do you want to play? 1 for random number guessing game/ 2 for rock, paper, scissors/ 3 for a coin flip.")
        if seleccion == "1":
            number_guessing_game()
            keep_playing_all()
        elif seleccion == "2":
            rock_paper_scissors()
            keep_playing_all()
        elif seleccion == "3":
            play_coin_flip()
            keep_playing_all()




def keep_playing_all():
    keep_playing = input("¿Do you want to play another game? y for yes, n for no")
    if keep_playing == "y":
        seguir_jugando = True
    elif keep_playing == "n":
        seguir_jugando = False
    else:
        print("That's not a valid option. Try again.")
        keep_playing_all()  

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Generate a random number between 1 and 10
        random_number = random.randint(1, 10)

        # Ask the user for a guess
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                if guess < 1 or guess > 10:
                    print("Please enter a number between 1 and 10.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Check if the guess is correct
        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
        else:
            print("Sorry, you guessed the wrong number. The correct number was", random_number)

        # Ask the user if they want to keep playing
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thank you for playing the Number Guessing Game!")


def rock_paper_scissors():
    print("Let's play Rock-Paper-Scissors!")
    choices = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ")
        player_choice = player_choice.lower()
        if player_choice in choices:
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")
            if player_choice == computer_choice:
                print("It's a tie!")
            elif (
                (player_choice == "rock" and computer_choice == "scissors") or
                (player_choice == "paper" and computer_choice == "rock") or
                (player_choice == "scissors" and computer_choice == "paper")
            ):
                print("You win!")
            else:
                print("Computer wins!")
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        
        choice = input("Do you want to play again? (y/n): ")
        if choice.lower() != 'y':
            break

def play_coin_flip():
    print("Welcome to the Coin Flip Game!")
    flip = random.choice(["Heads", "Tails"])
    guess = input("Enter your guess (Heads/Tails): ").capitalize()

    print(f"The coin flip result is: {flip}")

    if guess == flip:
        print("Congratulations! You guessed it correctly!")
    else:
        print("Sorry, you didn't guess correctly. Try again!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_coin_flip()

play_chipiado()