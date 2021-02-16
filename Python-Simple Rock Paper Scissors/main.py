import random

# Welcome
# Input Players move
# Generate Random Counter Move
# Compare Answers
# Get Winner
# Display Result

def main():
	while True:
		print('WELCOME TO A GAME OF ROCK PAPER SCISSORS\n')

		move_list = ['Rock', 'Paper', 'Scissor']
		ai_choice = random.choice(move_list)
		ai_choice_lower = str(ai_choice.lower())

		player_move = input("Rock, Paper or Scissor? >")
		player_move = player_move.strip()
		player_move_lower = player_move.lower()
		player_move_lower = str(player_move_lower)

		if player_move_lower == ai_choice_lower:
			print("It's a draw!")
			print(f'You both picked {player_move}')

		elif player_move_lower == 'paper' and ai_choice_lower == 'rock':
			print("AI Wins!")
			print(f"You picked {player_move} and AI picked {ai_choice}")

		elif player_move_lower == 'paper' and ai_choice_lower == 'scissor':
			print("AI Wins!")
			print(f"You picked {player_move} and AI picked {ai_choice}")

		elif player_move_lower == 'rock' and ai_choice_lower == 'paper':
			print("AI Win!")
			print(f"You picked {player_move} and AI picked {ai_choice}")

		elif player_move_lower == 'rock' and ai_choice_lower == 'scissor':
			print("You Win!")
			print(f"You picked {player_move} and AI picked {ai_choice}")

		elif player_move_lower == 'scissor' and ai_choice_lower == 'rock':
			print("AI Win!")
			print(f"You picked {player_move} and AI picked {ai_choice}")

		elif player_move_lower == 'scissor' and ai_choice_lower == 'paper':
			print("You Win!")
			print(f"You picked {player_move} and AI picked {ai_choice}")

		elif player_move_lower == 'quit' or 'exit':
			exit()

		else:
			print('What did you just input?')

		print('')

if __name__ == '__main__':
	main()
