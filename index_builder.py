import os
from word_frequencies import Text
import json
from collections import defaultdict
import tf_idf as ti

class Inverter(object):
	"""docstring for Inverter"""
	def __init__(self, path):
		with open(path + '/bookkeeping.json', 'r') as f:
			json_str = f.read()
			self.bookkeeping = json.loads(json_str)
		self.path = path
		self.index = defaultdict(list)
		self.index_builder()
		self.write2json()

		
	def index_builder(self):
		#build Inverted Index, do not return anything
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
							posting = []
							posting.append(i + '/' + file)#self.bookkeeping[i + '/' + file]
							posting.append(token[1]) # positions
							self.index[token[0]].append(posting)
		for term in self.index.values():
			for posting in term:
				posting.append(ti.tf_idf_score(len(posting[1]), N, len(term)))
		self.index['__N__'] = N
		

	def write2json(self):
		with open('index.json', 'w') as f:
			f.write(json.dumps(self.index))



if __name__ == '__main__':
	path = 'WEBPAGES_CLEAN'
	Inverter(path)

