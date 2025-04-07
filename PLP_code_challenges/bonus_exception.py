#!/usr/bin/env python3
"""
Write a Python program that:
Asks the user for a sentence using input()
Converts it to uppercase
Counts the number of words
Prints both results
"""
def upper_count():
    try:
        content = input("Please enter a sentence: ").strip()
        if not content:
            raise ValueError("Input cannot be empty.")
        # Check if the input is a valid string
        if not any(char.isalpha() for char in content):
            raise ValueError("Input must include at least one letter")
        
        # Convert to uppercase and count words
        content = content.upper()
        word_count = len(content.strip().split())
    except ValueError as e:
        print(f"Error: {e}")
        content = ""
        word_count = 0
        
    finally:
            print("The content in uppercase is:\n", content)
            print("The number of words is:\n", word_count)


if __name__ == "__main__":
	upper_count()