import json
from word_frequencies import Text
import tf_idf as ti
import sys

def query(string):
	with open('index.json', 'r') as f:
		index = json.loads(f.read())
	keywords = Text(None, string).computeWordFrequencies()
	L = len(keywords)
	query_score = 1
	query_vec = [0] * len(keywords)
	for i, keyword in enumerate(keywords.items()):
		query_vec[i] = ti.tf_idf_score(keyword[1], index['__N__'], len(index[keyword[0]]))
	print(query_vec)


if __name__ == '__main__':
	query(sys.argv[1])