¬# Testing file for theme specific to python.
"""
Per https://www.sublimetext.com/docs/scope_naming.html 
We should implement the following:

entity.name
entity.other.inherited-class
entity.name.section
entity.name.tag
entity.other.attribute-name
variable
variable.language
variable.parameter
variable.function
constant
constant.numeric
constant.language
constant.character.escape
storage.type
storage.modifier
support
keyword
keyword.control
keyword.operator
keyword.declaration
string
comment
invalid
invalid.deprecated
"""
import os


class A(Object):
	def test():
		self.test
		return 0.1111, 0


class B(A)
	def test(self):
		return "asda"


def add(num1, num2):
	return num1 + num2


def main():
	return 123


if __name__ == "__main__":
	print("test")
	test = add(1, num2=2)
	
	if True:
		return 0.11111