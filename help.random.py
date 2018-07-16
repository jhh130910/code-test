"""Generates Random Sentences

Creates a sentence by selecting a word at randowm from each of the lists in
    the following order: 'article', 'nounce', 'verb', 'preposition',
    'article' and 'noun'.

    The second part produce a short story consisting of several of
    these sentences -- Random Note Writer!!
"""

import random
article = ["the", "any"]
noun = ["boy", "girl"]
verb = ["drove", "jumped"]
preposition = ["to", "from"]

def random_int():
  return random.randint(0,1)

def random_sentence():
    """Creates random and return sentences."""
    return ("{} {} {} {} {} {}"
                .format(article[random_int()]
                        ,noun[random_int()]
                        ,verb[random_int()]
                        ,preposition[random_int()]
                        , article[random_int()]
                        ,noun[random_int()])).capitalize()
    
# prints random sentences
for sentence in list(map(lambda x: random_sentence(), range(0, 20))):
  print(sentence)
print("\n")

story = (". ").join(list(map(lambda x: random_sentence(), range(0, 20))))
# prints random sentences story
print("{}".format(story))
