import json
from word_frequencies import Text
import tf_idf as ti
import sys
import math
import heapq

class search_engine():
	def __init__(self):
		with open('index.json', 'r') as f:
			self.index = json.loads(f.read())
		path = 'WEBPAGES_CLEAN'
		with open(path + '/bookkeeping.json', 'r') as f:
			json_str = f.read()
			self.bookkeeping = json.loads(json_str)

	def cosine_similarity(self, v1, v2):
	    #compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)
	    # cited from https://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists
	    sumxx, sumxy, sumyy = 0, 0, 0
	    for i in range(len(v1)):
	        x = v1[i]; y = v2[i]
	        sumxx += x*x
	        sumyy += y*y
	        sumxy += x*y
	    return sumxy/math.sqrt(sumxx*sumyy)

	def docID2URL(self, docID):
		return self.bookkeeping[docID]

	def query(self, string):
		keywords = Text(None, string).computeWordFrequencies()
		L = len(keywords)
		query_score = 1
		query_vec = [0] * len(keywords)
		hits = {}
		for i, keyword in enumerate(keywords.items()):
			query_vec[i] = ti.tf_idf_score(keyword[1], self.index['__N__'], len(self.index[keyword[0]]))
			for posting in self.index[keyword[0]]:
				hits.setdefault(posting[0], [0] * len(keywords))
				hits[posting[0]][i] = float(posting[2])
		ranked_hits = heapq.nlargest(5, hits, key = lambda posting : self.cosine_similarity(query_vec, hits[posting]))

		return list(map(self.docID2URL, ranked_hits))
		'''h = []
					for posting in hits.items():
						heapq.heappush(h, (cosine_similarity(query_vec, posting[1]), posting[0]))'''


if __name__ == '__main__':
	se = search_engine()
	try:
		while True:
			print('Type a query:')
			query = input()
			print()
			print(se.query(query))
			print()
	except KeyboardInterrupt as e:
		print('\nExit.')
	except Exception as e:
		print(e)

