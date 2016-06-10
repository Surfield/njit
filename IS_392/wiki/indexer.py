import os
from lxml.html.clean import Cleaner
import re
from collections import Counter
import csv
import sys

csv.field_size_limit(sys.maxsize)

def load_stop_words():
	container = []
	with open("stopwords.csv", "r") as f:
		container = f.read().lower().split(",")
	f.closed
	return container

def read_file(file):
	html = ''
	with open(file, "r") as f:
		html = f.read()
	
	cleaner = Cleaner(allow_tags=[''], remove_unknown_tags=False)
	cleaned_text = cleaner.clean_html(html)
	return " ".join(cleaned_text.split())


def dictionary_write(hash, filename):
	writer = csv.writer(open(str(filename)+'.csv', 'wb'))
	for key, value in hash.items():
   		writer.writerow([key, value])

def dictionary_read(filename):
	reader = csv.reader(open(str(filename)+'.csv', 'rb'))
	return dict(reader)

def index():
	stop_words = load_stop_words()
	doc_counter = 0
	file_id = {}
	word_frequencies = {}
	word_locations = {}
	for file in os.listdir("../html"):
		if file.endswith(".html"):
			file_id[doc_counter] = file
			text = read_file("../html/"+file)
			word_position = 0
			for word in text.lower().split():
				if word not in stop_words:
					#handles frequency counting
					clean_word =  re.sub('[.?{}";|\(),]', '', word)
					word_frequencies.setdefault(clean_word, {})
					word_frequencies[clean_word].setdefault(doc_counter, 0)
					word_frequencies[clean_word][doc_counter] += 1

					#handles position tracking
					word_locations.setdefault(clean_word, [])
					word_locations[clean_word].append({doc_counter: word_position})

				word_position += 1
		doc_counter += 1

	dictionary_write(file_id, "file_id")
	dictionary_write(word_frequencies, "frequencies")
	dictionary_write(word_locations, "positions")

index()
