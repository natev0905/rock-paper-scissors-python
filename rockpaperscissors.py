#imoprot random to generate computer plays
import random
#set beginnig variables and lists
plays = ["ROCK","PAPER","SCISSORS"]
humanWins = [-2, 1]
humanCount = 0
computerCount = 0

def getValidHumanPlay( low, high ):
	#ask for input from the user and store it in a variable - "Enter 0 for Rock, 1 for Paper, 2 for Scissors"

	human_play = int(input("Please ener 0 for ROCK, 1 for PAPER or 2 for SCISSORS: "))
	#validate the players input to make sure it is in between 0 and 2. 
	if human_play >= low and human_play <= high:
		number_entered = True
	else:
		number_entered = False
		print("You did not enter a number 1, 2 or 3")
	#using a while loop, if the input for the user is incorrect, redo the first few steps and reenter a play
	while number_entered == False:
		human_play = int(input("Please ener 0 for ROCK, 1 for PAPER or 2 for SCISSORS"))
		if human_play >= low and human_play <= high:
			number_entered = True
		else:
			number_entered = False
		print("You did not enter a number 1, 2 or 3")
	#return the input from the user when it is valid
	return human_play

	
	
	

def getPlay( human, plays ):
	global humanPlay, computerPlay
	#creates the humanPlay variable and sets the function low and high values in a variable
	humanPlay = getValidHumanPlay(0,2)
	#Creates the computerPlay variable and lets a randomizer pick the computers option (0,2)
	computerPlay = random.randint(0,2)
	#prints out the what the human chose to play
	print(human, "picked" , plays[humanPlay])
	#print what computer/randomizer chose to play
	print("Computer picked ", plays[computerPlay])
	#check if they tied and returning the values

	return humanPlay
	return computerPlay


### Beginning of Main

#enter users name to be used during game
human = input( "Enter your name ").upper()

#introduce new boolean variable
keepPlaying = True

while keepPlaying:
	#create a variable called play and call the getPlay function, sending human and plays variable
	play = getPlay(human, plays)
	#finding the result
	result = humanPlay - computerPlay
	if result in humanWins:
		#add 1 to the human side
		humanCount += 1
		#print off winning message
		print(human, "won by playing ", plays[humanPlay], ",which beat ", plays[computerPlay])
	#to check for a tie
	elif result == 0:
		print("There has been a tie, both picked ", plays[humanPlay])
	else:
		#if the computer wins, add 1 to its score
		computerCount += 1
		#print winning message for computer
		print("Computer won by playing ", plays[computerPlay], ", which beat", plays[humanPlay])
	#print the score as of now
	print(humanCount, computerCount)
	#check if each score is less than 3, end game if one of them reaches 3 or more
	if computerCount >= 3 or humanCount >= 3:
		keepPlaying = False


#create an if-statement (not inside the while loop) that checks if the human has won 3 times
if humanCount == 3:
	
	#if the human has won 3 times declare that they have won the match and display humanCount to computerCount
	print(human, "has won the full game: ", humanCount, "to", computerCount)
#else if the computer has won, declare they have won the match and display computerCount to humanCount
else:
	print("Computer has won the full game:", computerCount, "to", humanCount)

