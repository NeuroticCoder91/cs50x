# A program that calculates the grade level of a text

# Imports
from cs50 import get_string
import re

# Get user's text
text = get_string("Text: ")

# Count sentences using . ! ? as checks
sentences = len(re.findall(r'[.!?]', text))

# Count words by counting spaces; add 1 for first word
words = len(re.findall(r'\s', text)) + 1

# Count letters; case-insensitive
letters = len(re.findall(r'[a-zA-Z]', text))

# Calculate Liau's index
S = sentences / words * 100
L = letters / words * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade", index)
