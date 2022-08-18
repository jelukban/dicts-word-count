"""Count words in file."""


def tokenize(filename):
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

# print(tokenize("twain.txt"))