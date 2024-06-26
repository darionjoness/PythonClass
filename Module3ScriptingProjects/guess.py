import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

minGuesses = math.ceil(math.log2(larger - smaller + 1))
print(f"Guess the number in at most {minGuesses} guesses.")

low = smaller
high = larger
attempts = 0

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    print(f"Guess: {guess}")
    feedback = input("Enter 'high' if the guess is too high, 'low' if it is too low, and 'correct' if it is correct: ").strip().lower()
    
    if feedback == 'correct':
        print(f"Guessed {guess} in {attempts} attempts!")
        break
    elif feedback == 'low':
        low = guess + 1
    elif feedback == 'high':
        high = guess - 1
    else:
        print("Incorrect input. Enter 'high', 'low', or 'correct'.")
    
    if low > high:
        print("Incorrect hint. Please start over and provide correct hints.")
        break
