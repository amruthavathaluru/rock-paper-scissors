import tkinter as tk
import random
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"
def handle_player_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    play_again_button.pack()
def play_again():
    result_label.config(text="")
    play_again_button.pack_forget()
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instruction_label.pack()
rock_button = tk.Button(root, text="Rock", command=lambda: handle_player_choice("Rock"))
rock_button.pack()
paper_button = tk.Button(root, text="Paper", command=lambda: handle_player_choice("Paper"))
paper_button.pack()
scissors_button = tk.Button(root, text="Scissors", command=lambda: handle_player_choice("Scissors"))
scissors_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
play_again_button = tk.Button(root, text="Play Again", command=play_again)
root.mainloop()
