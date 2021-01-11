
f = open('characters.txt','r')
characters = [x.strip('\n') for x in f.readlines()]

f = open('rooms.txt','r')
rooms = [x.strip('\n') for x in f.readlines()]

f = open('items.txt','r')
items = [x.strip('\n') for x in f.readlines()]

# f = open('verb_to.txt','r')
# verb_to = [x.strip('\n') for x in f.readlines()]

f = open('sentences.txt','r')
sentences = [x.strip('\n') for x in f.readlines()]

import random as rand

# rand.choice() # with replacement
# rand.sample() #without replacement

def capitalizer(s):
	return s[0].capitalize() + s[1:]

novel = ''
nb_sentences = 10

objects = {
	'CHARACTER': characters,
	'ROOM':rooms,
	# 'VERB_TO': verb_to,
	'ITEM': items
}

for _ in range(nb_sentences):

	used = set() # we keep track of characters/items/verbs used so we don't reuse them in the sentence
	# Pick a sentence
	sentence = rand.choice(sentences)

	# for each thing to replace
	for object_type, object_choices in objects.items():
		while object_type in sentence:
			choice = None
			while choice in used or choice is None:
				choice = rand.choice(object_choices)
			sentence = sentence.replace(object_type, choice, 1)
			used.add(choice)

	# Add to novel
	novel += '\n' + capitalizer(sentence)

print(novel)

# IDEAS

# Each room can have features
# A color,
# A temperature/moisture
# Other (dusty, sparkling clean, decorated,brightly lit, web covered, candle.lit, moonlight lit, 
# A small

# TODO:
# implement verbs
# implement adverbs
# capitalize first words
# make sure character not picked in same sentence
# randomly replace "a" or "an" with "the"