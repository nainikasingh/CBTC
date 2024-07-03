import random


def generate_number(length):
    return ''.join(random.choices('0123456789', k=length))


def get_hint(secret, guess):
    correct_digits = sum(s == g for s, g in zip(secret, guess))
    correct_numbers = sum(min(secret.count(n), guess.count(n)) for n in set(guess)) - correct_digits
    return correct_digits, correct_numbers


def play_round(player, secret_length):
    secret = generate_number(secret_length)
    attempts = 0

    print(f"{player} has set the number.")

    while True:
        guess = input(f"{player}, enter your guess: ")
        attempts += 1

        if guess == secret:
            print(f"Correct! The number was {secret}. It took {attempts} attempts.")
            return attempts
        else:
            correct_digits, correct_numbers = get_hint(secret, guess)
            print(f"Hint: {correct_digits} digits are correct and in the correct position.")
            print(f"{correct_numbers} digits are correct but in the wrong position.")


def main():
    print("Welcome to MASTERMIND!")
    secret_length = int(input("Enter the length of the secret number: "))

    print("\nPlayer 1's turn to set the number.")
    attempts_p1 = play_round("Player 2", secret_length)

    print("\nPlayer 2's turn to set the number.")
    attempts_p2 = play_round("Player 1", secret_length)

    if attempts_p1 < attempts_p2:
        print("\nPlayer 1 wins and is crowned Mastermind!")
    else:
        print("\nPlayer 2 wins and is crowned Mastermind!")


if __name__ == "__main__":
    main()
