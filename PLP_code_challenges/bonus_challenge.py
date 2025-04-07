#!/usr/bin/env python3
"""
Write a Python program that:
Asks the user for a sentence using input()
Converts it to uppercase
Counts the number of words
Prints both results
"""
def upper_count():
	content = input("Please enter a sentence: ")
	# Convert to uppercase and count words
	content = content.upper()
	word_count = len(content.strip().split())


	print("The content in uppercase is:\n", content)
	print("The number of words is:\n", word_count)

if __name__ == "__main__":
	upper_count()