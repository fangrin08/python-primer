import math

some_text = "1a2b3c4d"

def is_letter(texts):
	if texts in "abcdefg":
		return True
	else:
		return False

def extract_letters(text):
	s = ""
	for c in text:
		if is_letter(c):
			s = s + c
			print("partial = " + s)
		else:
			print(c + " is a number!")
	return s

letters = extract_letters(some_text)

print("FINAL = " + letters)
