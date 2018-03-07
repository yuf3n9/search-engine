import json
from word_frequencies import Text
import tf_idf as ti
import sys
import math
import heapq
from collections import defaultdict

class search_engine():
	def __init__(self):
		with open('index.json', 'r') as f:
			self.index = json.loads(f.read())
		self.path = 'WEBPAGES_CLEAN/'
		with open(self.path + 'bookkeeping.json', 'r') as f:
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
		snippet_position = defaultdict(list)
		for i, keyword in enumerate(keywords.items()):
			try:
				query_vec[i] = ti.tf_idf_score(keyword[1], self.index['__N__'], len(self.index[keyword[0]]))
				for posting in self.index[keyword[0]]:
					hits.setdefault(posting[0], [0] * len(keywords))
					hits[posting[0]][i] = float(posting[2])
					snippet_position[posting[0]] = posting[1]
			except KeyError as e:
				pass
		#ranked_hits = heapq.nlargest(5, hits, key = lambda posting : self.cosine_similarity(query_vec, hits[posting]))
		ranked_hits = heapq.nlargest(5, hits, key = lambda posting : sum(hits[posting]))
		ranked_snippet_position = [snippet_position[hit] for hit in ranked_hits]
		ranked_snippet = []
		for i, hit in enumerate(ranked_hits):
			snippet = []
			content = Text(self.path + hit).tokenize()
			for pos in ranked_snippet_position[i][:2]: #limit to 2 here. need to modify
				snippet.append(content[pos-15:pos+15] if pos >= 15 else content[0:pos+15])
			ranked_snippet.append(snippet)

		return list(map(self.docID2URL, ranked_hits)), ranked_snippet
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
			hits, snippets = se.query(query)
			for i in range(len(hits)):
				print(hits[i])
				for snippet in snippets[i][:2]:
					print(' '.join(snippet))
				print('---------------------------------------')
			print()
	except KeyboardInterrupt as e:
		print('\nExit.')
	except Exception as e:
		print(e)

