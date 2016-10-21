import math

some_text = "1a2b3c4d"

def is_number(num):
	if num in "1234567890":
		return True
	else:
		return False

def extract_numbers(text):
	s = ""
	for c in text:
		if is_number(c):
			s = s + c
			print("partial = " + s)
		else:
			print(c + " is not a number!")
	return s

numbers = extract_numbers(some_text)

print("FINAL = " + numbers)