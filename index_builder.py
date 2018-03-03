class Inverter(object):
	"""docstring for Inverter"""
	def __init__(self, path):
		self.path = path
		self.index = None
		self.index_builder()

		
	def index_builder(self):
		#build Inverted Index, do not return anything
		

	def tf_weight(self, tf):
		#return tf weight


	def idf_weight(self, term):
		#return idf weight


	def tf_idf_score(self, query, doc):
		'''
		:type query: List[str] - a list of terms

		return tf_idf_score
		'''


	def query(key_words):
		'''
		:type key_words: List[str]
		:rtype: List[str] - a list of ranked URLs
		'''

		