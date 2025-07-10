import random
words=["apple","banana","mango","orange","grape"]
word=random.choice(words)
guessed=["_"]*len(word)
attempts=6
guessed_letters=[]
print("Welcome to Hangaman! ")
while attempts>0 and "_" in guessed:
    print("\nWord:"," ".join(guessed))
    print(f"Attempts left {attempts}")
    guess=input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.Try another ")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
        print("Good Guess! ")
    else:
        attempts-=1
        print("Incorrect Guess .")
if "_" not in guessed:
    print(f"You guessed the word {word}")
else:
    print(f"Game Over.The word was {word}")