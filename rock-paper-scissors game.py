import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices list
choices = ['rock', 'paper', 'scissors']

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    global user_score, computer_score

    print("\n🎮 Welcome to Rock, Paper, Scissors Game! 🎮")

    while True:
        # Prompt user for input
        user_choice = input("\nChoose rock, paper, or scissors (or type 'exit' to quit): ").lower()

        if user_choice == "exit":
            print("\n👋 Thanks for playing!")
            print(f"🏆 Final Scores → You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in choices:
            print("❌ Invalid choice. Please try again.")
            continue

        # Generate computer choice
        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

        # Determine winner
        result = get_winner(user_choice, computer_choice)

        # Show results
        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ You lose this round.")
            computer_score += 1

        # Display current scores
        print(f"📊 Score → You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        again = input("\n🔁 Play another round? (yes/no): ").lower()
        if again != 'yes':
            print("\n👋 Thanks for playing!")
            print(f"🏆 Final Scores → You: {user_score} | Computer: {computer_score}")
            break

# Run the game
play_game()
