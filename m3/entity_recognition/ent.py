
import spacy
import json


tweets = json.loads(open('../../dataset/lbiden.json').read())
nlp = spacy.load('en_core_web_sm')
entities = {}


def show_entities(tweet):
	ents = []
	if len(tweet.ents) > 0:
		for entity in tweet.ents:
			ent = (entity.text, entity.label_, spacy.explain(entity.label_))
			ents.append(ent)
	return ents


for t in range(len(tweets)):
	tweet = nlp(tweets[t])
	entities[t] = show_entities(tweet)

individuals = set()

for i in entities:
	ent = entities[i]
	for j in range(len(ent)):
		if ent[j][1] == 'PERSON':
			individuals.add(ent[j][0])

for person in individuals:
	print(person)