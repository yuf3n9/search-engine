import fire
import re
from collections import Counter

class Text:
	def __init__(self, path):
		with open(path, 'r') as f:
			#\W == [^a-zA-Z0-9_], which excludes all numbers, letters and _
			self.s = re.sub(r'[\W_]+', ' ', f.read().replace("'",'')).lower()	#may use read(size) to avoid OOM for large inputs

	def tokenize(self):
		return self.s.split()

	def computeWordFrequencies(self):
		return Counter(self.tokenize())

	def printFrequencies(self):
		for item in self.computeWordFrequencies().most_common():
			print(item[0] + ', ' + str(item[1]))
		#print(self.computeWordFrequencies().most_common())

	def run(self):
		self.printFrequencies()

if __name__ == '__main__':
	fire.Fire(Text)