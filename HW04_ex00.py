#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
from random import randint

# Body


def guessing_game():

	# create random integer
	rand_int = randint(1,25)

	# set n = 1 as a counting measure for number of tries
	n = 1

	while True:
		user_number = raw_input("Enter a number pretty prease... you only have 5 tries-- ")
		try:
			user_int = int(user_number)
		except:
			print "\nThat's not a number foo...\n"
		else:
			# if guessed correctly then break
			if rand_int==user_int:
				break_answer = "\nYou win an Xbox 1 and a GameCube!\n"
				break
			# if didn't guess correct, then give one of three options
			else:
				# if five tries, then game over
				if n == 5:
					break_answer = "\nsorry game over.. the answer was " + str(rand_int) + " NERD!"
					break
				# if user guess too high... add 1 to n
				if user_int > rand_int:
					print "\nTOO HIGH!"
					print "loser...that was try number " + str(n) + ". Go again\n"
					n += 1
				# if user guess too low... add 1 to n
				elif user_int < rand_int:
					print "\nTOO LOW!"
					print "loser...that was try number " + str(n) + ". Go again\n"
					n += 1
	# print message when user either wins or loses
	print break_answer

################################################################################
def main():


    guessing_game()
    

if __name__ == '__main__':
    main()