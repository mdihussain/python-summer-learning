#MD Hussain
#Practice day

def add_list_of_numbers(x):
    total = 0
    for a in x:
        total += a
    return total
    


def string_character_count(s):
    character_dictionary = {}

    for char in s:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else: character_dictionary[char] = 1

    return character_dictionary

def word_counts(s):
    words = s.split()
    word_count_dictionary = {}

    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else: word_count_dictionary[word] = 1

    return word_count_dictionary

#doesn't work when there's punctuation marks involved

import string

def new_word_counts(s):

    translator_table = str.maketrans("", "", string.punctuation)
    #this is making a table that's like we don't want to replace anything[""],
    #with anything[""]... but we want to delete all punctuations
    s = s.translate(translator_table)
    words = s.split()
    word_count_dictionary = {}

    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else: word_count_dictionary[word] = 1

    return word_count_dictionary

 #now "you're" comes out as "youre"... aaaa...anyway

def newer_word_counts(s):

    translator_table = str.maketrans("", "", "!#$%&\()*+,-./:;<\"=>?@[\\]^_`{|}~")
    #this is making a table that's like we don't want to replace anything[""],
    #with anything[""]... but we want to delete all punctuations
    s = s.translate(translator_table)
    words = s.split()
    word_count_dictionary = {}

    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else: word_count_dictionary[word] = 1

    return word_count_dictionary
