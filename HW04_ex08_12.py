# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

def rotate(string, number):
	for index in string:
		
		# add number input to the ord of the current item
		new_char_num = ord(index) + number
		#print chr(new_char_num)

		# create a while loop that subtracts 26 to any number lower than 122
		while new_char_num > 122:
			new_char_num -= 26

		# create a while loop that add 26 to any number lower than 97
		while new_char_num < 97:
			new_char_num += 26

		# print chr of new number
		print chr(new_char_num)
		

rotate("melon",-36)

rotate("cheer", 26*7 + 7)