#!/usr/bin/python3
"""python Function to write text to file and
   returns number of characters written
"""


def write_file(filename="", text=""):
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(text)
		return len(text)
