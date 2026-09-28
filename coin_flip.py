import random


def coin_flip_game():
    print("🪙 Welcome to Coin Flip Duel!")
    print("Pick heads or tails and see if you can beat the computer.")

    while True:
        try:
            rounds = int(input("How many rounds would you like to play? "))
            if rounds > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    player_score = 0
    computer_score = 0

    for round_number in range(1, rounds + 1):
        while True:
            choice = input(f"Round {round_number}: heads or tails? ").strip().lower()
            if choice in {"heads", "tails"}:
                break
            print("Invalid choice. Enter 'heads' or 'tails'.")

        result = random.choice(["heads", "tails"])
        print(f"The coin landed on: {result}")

        if choice == result:
            print("You win this round! 🎉")
            player_score += 1
        else:
            print("Computer wins this round. 🤖")
            computer_score += 1

    print("\nFinal score:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")

    if player_score > computer_score:
        print("You won the match! 🏆")
    elif computer_score > player_score:
        print("The computer won this time. Better luck next round!")
    else:
        print("It's a tie! ⚖️")


if __name__ == "__main__":
    coin_flip_game()
