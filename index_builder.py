import os
from word_frequencies import Text
import json
from collections import defaultdict
import math

class Inverter(object):
	"""docstring for Inverter"""
	def __init__(self, path):
		with open(path + '/bookkeeping.json', 'r') as f:
			json_str = f.read()
			self.bookkeeping = json.loads(json_str)
		self.path = path
		self.index = []
		self.index_builder()
		self.write2json()

		
	def index_builder(self):
		#build Inverted Index, do not return anything
		terms = defaultdict(list)
		dirlist = os.listdir(self.path)
		N = 0
		for i in dirlist:
			dir = os.path.join(self.path, i)
			if not os.path.isfile(dir):
				filelist = os.listdir(dir)
				for file in filelist:
					filepath = os.path.join(dir, file)
					if os.path.isfile(filepath):
						N += 1
						tokens = Text(filepath).wordPosition()
						for token in tokens.items():
							post = []
							post.append(i + '/' + file)#self.bookkeeping[i + '/' + file]
							post.append(token[1])
							terms[token[0]].append(post)

		print(json.dumps(terms))
		#print(os.path.walk(self.path))
		

	def tf_weight(self, tf):
		#type tf: int
		#return tf weight
		return 0 if not tf else 1 + math.log10(tf)


	def idf_weight(self, N, df):
		#type term: str
		#return idf weight
		return math.log10(N/df)


	def tf_idf_score(self, query, doc):
		'''
		:type query: List[str] - a list of terms
		return tf_idf_score
		'''
		pass


	def write2json(self):
		pass


	def query(self, key_words):
		'''
		:type key_words: List[str]
		:rtype: List[str] - a list of ranked URLs
		'''

if __name__ == '__main__':
	path = 'WEBPAGES_CLEAN'
	Inverter(path)

