#!/usr/bin/python3

import re
from collections import defaultdict

# Function to get the most and least used words
def get_most_least_used_words(word_counts):
    max_count = max(word_counts.values())
    min_count = min(word_counts.values())
    
    most_used = [word for word, count in word_counts.items() if count == max_count]
    least_used = [word for word, count in word_counts.items() if count == min_count]
    
    return most_used, least_used

def main():
    # Get the file name from user input
    files = input("Enter the file: ")
    
    # Create a dictionary to hold word counts
    word_counts = defaultdict(int)
    
    # Open and read the file contents
    with open(files, 'r', newline='') as file:
        file_contents = file.read()
    
    # Split the contents into words using regular expression
    words = re.split(r'\W+', file_contents, flags=re.IGNORECASE)
    
    # Count the occurrences of each word
    for word in words:
        if word:  # Ignore empty strings
            word_counts[word.lower()] += 1  # Convert to lowercase to make the count case-insensitive
    
    # Print the word counts alphabetically
    for word in sorted(word_counts):
        print(f"({word}: {word_counts[word]})", end=" ")
    print()  # Print a newline at the end
    
    # Get and print the most and least used words
    most_used, least_used = get_most_least_used_words(word_counts)
    print("Most used words:", ', '.join(most_used))
    print("Least used words:", ', '.join(least_used))

if __name__ == "__main__":
    main()
