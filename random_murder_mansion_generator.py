import random as rand
# rand.choice() # with replacement
# rand.sample() #without replacement
import argparse

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

def capitalizer(s):
	return s[0].capitalize() + s[1:]

objects = {
	'CHARACTER': characters,
	'ROOM':rooms,
	# 'VERB_TO': verb_to,
	'ITEM': items
}


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Write a murder mystery with certain chacracteristics.")
	parser.add_argument("--seed", type=int, help="The random seed.", default=None)
	parser.add_argument("-n", type=int, help="The number of sentences.", default=10)
	args = parser.parse_args()
	print("here")

	nb_sentences = args.n
	if args.seed:
		rand.seed(args.seed)

	novel = "\n"
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

# Perhaps we have an option to create the novel with a randomly set cast of character/rooms/items
# so that the repetition creates interesting connections in the reader's mind
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