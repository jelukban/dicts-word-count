"""Count words in file."""
import sys
from typing import final

def tokenize(filename = sys.argv[1]):
  """ Takes in a file and returns a list of each word in the text file
  """
  input_text = open(filename)
  list_of_words = []

  for line in input_text:
    words = line.rstrip().split(' ')

    for word in words:
      if not word:
        continue

      if word[-1] in ",./]}!?'[{(-" or word[-1] in '"':
        word = word[:-1]
      elif word[0] in ",./]}!?'[{(-" or word[-1] in '"':
        word = word[1:]

      list_of_words.append(word)

  input_text.close()
  return list_of_words

# print(tokenize())

def count_words(words = tokenize()):
  """ Takes in a list of strings and returns a dictionary of each string and its occurrence
  """

  final_word_dict = {}

  for word in words:
    word = word.lower()

    final_word_dict[word] = final_word_dict.get(word, 0) + 1

  return final_word_dict

# print(count_words())

def print_word_counts(words = count_words()):
  """Takes in a dictionary of words and their occurence, prints out the key and value"""

  for key, value in words.items():
    print(f"{key} {value}")

print(print_word_counts())