import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update the result and scores in the UI
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n{result}")
    score_label.config(text=f"Scores - You: {user_score} | Computer: {computer_score}")

# Reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text=f"Scores - You: {user_score} | Computer: {computer_score}")

# Create the main tkinter window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")
window.resizable(False, False)

# Initialize scores
user_score = 0
computer_score = 0

# Create UI elements
title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(window, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(window, text=f"Scores - You: {user_score} | Computer: {computer_score}", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Reset button
reset_button = tk.Button(window, text="Reset Game", width=15, command=reset_game)
reset_button.pack(pady=10)

# Run the tkinter main loop
window.mainloop()
