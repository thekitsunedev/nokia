#!/usr/bin/env python3
"""
This script prints out whether the lines in the file 'input.txt'
is palindrome or not.
Additionaly it returns the sum of unique characters in the string.

Usage: main.py

Author: TheKitsuneDev (Kis Vilmos Bendegúz)
Date: 2024.05
Event: nokia-hackathon
"""

with open('./input.txt', 'r') as f:
    for line in f:
        line = ''.join(char for char in line.strip().lower() if char.isalnum())
        inverted_line: str = line[::-1]
        characters: set = {character for character in line}
        if line == inverted_line:
            print(f"YES, {len(characters)}")
        else:
            print("NO, -1")