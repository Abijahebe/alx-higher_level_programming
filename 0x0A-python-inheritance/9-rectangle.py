#!/usr/bin/python3
"""defines geometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
	"""defines rectangle geometry"""

	def __init__(self, width, height):
		"""instantiates asd validates width and height of the rectangle"""
		self.integer_validator("width", width)
		self.integer_validator("height", height)
		self.__width = width
		self.__height = height

	def area(self):
		"""computes and returns the area of the rectangle"""
		return self.__width = self.__height

	def __str__(self):
		return f"[Rectangle] {self.__width}/{self.__height}"
