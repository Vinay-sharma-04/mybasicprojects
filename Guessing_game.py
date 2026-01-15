import random

easy_words = ['cat', 'dog', 'apple', 'ball', 'tree', 'apple', 'car', 'house', 'book', 'fish']
medium_words = ['python', 'guitar', 'elephant', 'mountain', 'computer', 'library', 'bicycle', 'jungle']
hard_words = ['xylophone', 'quizzical', 'juxtapose', 'zephyr', 'mnemonic', 'pharaoh', 'labyrinth', 'onomatopoeia']

print("Welcome to the password Guessing Game!")
print("Choose a difficulty level: easy, medium, hard ")

leval = input("Enter difficulty level: ").lower()

if leval == 'easy':
    secret = random.choice(easy_words)
elif leval == 'medium':
    secret = random.choice(medium_words) 
elif leval == 'hard':
    secret = random.choice(hard_words)      
else:
    print("Invalid choice. Defaulting to easy level.")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You've guessed the password '{secret}' in {attempts} attempts.")
        break
    
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:", hint)

print("Game over. Thanks for playing!")