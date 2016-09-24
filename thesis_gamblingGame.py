# Amanda Dobbyn
# Thesis gambling game
# 2014-2015

# This is a simplified version of the game used for my thesis that does not
# write output to a CSV file.

from random import randint

def setMultiplier(game, pot, randNum):
	if game == 1:
		if pot == 1:
			if randNum == 1:
				multiplier = 1.5
			if randNum == 2:
				multiplier = 1
			if randNum == 3:
				multiplier = 0.9
		if pot == 2:
			if randNum == 1:
				multiplier = 2
			if randNum == 2:
				multiplier = 1
			if randNum == 3:
				multiplier = 0.4
		if pot == 3:
			if randNum == 1:
				multiplier = 2.4
			if randNum == 2:
				multiplier = 1
			if randNum == 3:
				multiplier = 0
	if game == 2:
		if pot == 1:
			if randNum == 1:
				multiplier = 2
			if randNum == 2:
				multiplier = 1
			if randNum == 3:
				multiplier = 0.5
		if pot == 2:
			if randNum == 1:
				multiplier = 3
			if randNum == 2:
				multiplier = 1
			if randNum == 3:
				multiplier = 0.33333
		if pot == 3:
			if randNum == 1:
				multiplier = 4
			if randNum == 2:
				multiplier = 1
			if randNum == 3:
				multiplier = 0.25
	return multiplier


def gamble():
	total = 0 # Set total winnings to 0
	g = 1 # Set game to 1
	for g in range (1, 3): # 2 games total
		print "\n" + "\n" "This is game " + str(g) + "\n" + "\n"
		r = 1 # Set round to 1
		while r < 4:    # Rounds 1 to 3
			print "\n" + "\n" "This is round " + str(r) 
			for p in range (1, 4):
				their_input = float(raw_input("Bid for pot " + str(p) + " is: $"))    # Store their bid as a float in their_input
				rand = randint(1, 3)    # Pick random integer between 1 and 3, inclusive
				# print "Rand is " + str(rand)   # Wouldn't print this in the final script
				if their_input >= 0 and their_input <= 10:    # Check that their_input is between 0 and 10
					winnings = their_input*(float(setMultiplier(g, p, rand)))    # Winnings for that round are their_input*the output of setMultiplier
					total = total + winnings   
					avg = (total / 3)
					print "\n" + "Winnings for round " + str(r) + " is " + str(winnings) + "\n" + "\n" + "\n"
					r += 1    # Add one to our index
				else:
					print "\n" + "This amount is not valid. Please enter an amount that is greater than 0 and less than 10." + "\n" + "\n"
					# Now we want this to go back up and try that round again
					r -= 1  
		print "Total winnings for game " + str(g) + " are " + str(total) + "\n" + "\n" + "\n"
		print "Average winnings for game " + str(g) + " are " + str(avg) + "\n" + "\n" + "\n"

print(gamble())
