#!/usr/bin/python3
"""python Function to write text to file and
   returns number of characters written
"""


def write_file(filename="", text=""):
	"""writes a string to a text file (UTF8)

	Args:
		filename: name of the file
		text: string to write file

	Return:
		number of characters written to file
	"""
	if filename:
	with open(filename, 'w', encoding='utf-8') as writeFile:
		return writeFile.write(text)
