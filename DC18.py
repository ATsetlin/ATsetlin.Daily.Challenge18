	# ex at start password = abc
	# at end password = bcd

	# 1 convert input into list
	# 2 for loop that pulls ord value for every char
	# 3 convert list back to string
	# 4 output string

# ask for password input
password = input("Please select a password ")

# ask if to encript or decrcript
command = input("Would you like to Encript or Decript? (E/D) ")

# ask for a key valued @ 1-26
key = input("Please select a Key (1-26)")

for letter in password:
	letter = ord(letter)
	key_list.append(letter)	

# execute their selection
if command == "E" or "e":
		letter = letter + int(key)
		new_password = letter
elif command == "D" or "d":
		letter = letter - int(key)
		new_password = letter
else:
	print("Invalid. You will be stabbed in the back. Just like Caesar")	

print(new_password)

