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

      if word[-1] in ",./]}!?'[{(-":
        word = word[:-1]
      elif word[0] in ",./]}!?'[{(-":
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

    if word in final_word_dict:
      final_word_dict[word] += 1
    else:
      final_word_dict[word] = 1

  return final_word_dict

# print(count_words())