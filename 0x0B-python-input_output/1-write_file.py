#!/usr/bin/python3
"""contains a function that writes a string to a file"""


def write_file(filename="", text=""):
	"""writes a string to a text file (UTF8)

	Args:
		filename: name of file
		text: string to write to the file

	Return:
		number of chracters written to the file
	"""
	if filename:
		with open(filename, 'w', encoding='utf=8') as writefile:
			return writeFile.write(text)
