# MD Hussain
# Practice day

# Exercise 1.1: Write a function that takes a list of numbers as input, 
# and returns the sum of all the numbers in the list.
def add_list_of_numbers(x):
    total = 0
    for a in x:
        total += a
    return total

# Exercise 1.2: Write a function that takes a string as input, 
# and returns a dictionary where the keys are characters, 
# and the values are the number of times each character appeared in the input string.
def string_character_count(s):
    character_dictionary = {}

    for char in s:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else: character_dictionary[char] = 1

    return character_dictionary

# Exercise 1.3: Write a function that takes a string as input, 
# and returns a dictionary where the keys are words, 
# and the values are the number of times each word appeared in the input string.
def word_counts(s):
    words = s.split()
    word_count_dictionary = {}

    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else: word_count_dictionary[word] = 1

    return word_count_dictionary

# Enhanced version of Exercise 1.3: 
# It handles punctuation marks while considering the words in a string.
import string

def new_word_counts(s):

    translator_table = str.maketrans("", "", string.punctuation)
    s = s.translate(translator_table)
    words = s.split()
    word_count_dictionary = {}

    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else: word_count_dictionary[word] = 1

    return word_count_dictionary

# Further enhanced version of Exercise 1.3: 
# It excludes certain punctuation marks while considering the words in a string. 
def newer_word_counts(s):

    translator_table = str.maketrans("", "", "!#$%&\()*+,-./:;<\"=>?@[\\]^_`{|}~")
    s = s.translate(translator_table)
    words = s.split()
    word_count_dictionary = {}

    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else: word_count_dictionary[word] = 1

    return word_count_dictionary


#------------------------------------------------

# Md Hussian
# Use my_utils in a script

import my_utils

Numbers = [2,3,4,5,6]

# Use the function from my_utils to sum the numbers
total = my_utils.add_list_of_numbers(Numbers)
print(total)

# Use the function from my_utils to count the words in the given sentence
total_words = my_utils.newer_word_counts("the quick brown fox jumped over the lazy dog, crazy sight")
print(total_words)

# Use the function from my_utils to count the characters in the given sentence
total_characters = my_utils.string_character_count("the quick brown fox jumped over the lazy dog, crazy sight")
print(total_characters)

