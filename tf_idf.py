import math

def tf_weight(tf):
	#type tf: int
	#return tf weight
	return 0 if not tf else 1 + math.log10(tf)


def idf_weight(N, df):
	#type term: str
	#return idf weight
	return math.log10(N/df)


def tf_idf_score(tf, N, df):
	'''
	:type query: List[str] - a list of terms
	return tf_idf_score
	'''
	return tf_weight(tf) * idf_weight(N, df)