print("Welcome to my Apex Legends quiz!")

playing = input("Do you want to play? (yes/no) ").lower()  # Convert input to lowercase for consistency

if playing.lower() != "yes":
    quit()

print("OK! Let's play ;)")

score = 0  # Initialize score

# First Question
answer = input("What character in Apex Legends is a healer? ").strip()
if answer.lower() == "lifeline":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Second Question
answer = input("What's Apex Legends' first map? ").strip()
if answer.lower() == "king's canyon":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Third Question
answer = input("Who killed Loba's parents? ").strip()
if answer.lower() == "revenant":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Fourth Question
answer = input("Who has had the most nerfs since the game released? ").strip()
if answer.lower() == "wraith":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Display score
print(f"\nYour final score is {score}/4.")
if score == 4:
    print("Perfect score! You are an Apex Legends expert!")
elif score >= 2:
    print("Good job! You're on your way to becoming a legend!")
else:
    print("Better luck next time! Keep playing to improve!")
