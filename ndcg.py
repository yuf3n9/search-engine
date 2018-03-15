from googlesearch.googlesearch import GoogleSearch

def google(keywords):
	query = ['mondego', 'machine learning', 'software engineering', 'security', 'student affairs', 'graduate courses', \
			'Crista Lopes', 'REST', 'computer games', 'information retrieval']

	response = GoogleSearch().search(keywords + "site:ics.uci.edu", num_results = 100)
	url = [result.url for result in response.results]

	return url if url else []