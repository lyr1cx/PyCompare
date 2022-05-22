# Importing difflib
import difflib

with open('f1.txt') as file_1:
	file_1_text = file_1.readlines()

with open('f2.txt') as file_2:
	file_2_text = file_2.readlines()

# Find and print the diff:
for line in difflib.unified_diff(
		file_1_text, file_2_text, fromfile='f1.txt',
		tofile='f2.txt', lineterm=''):
	print(line)