#!/usr/bin/python3
"""contains a class that defines BaseGeometry"""


class BaseGeometry:
	"""defines geometry"""

	def area(self):
		"""raises an Exception"""
		raise Exception("area() is not implemented")

	def integer_validation(self, name, value):
		"""validation value"""
		if type(value) is not int:
			raise TypeError(f"{name} must be an integer")

		if value <= 0:
			raise ValueError(f"{name} must be greater than 0")
