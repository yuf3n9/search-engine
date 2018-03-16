from googlesearch.googlesearch import GoogleSearch
# written by Anthony Hseb and made compatible to py3 by notmikeb
# add more delay by myself to avoid request denial
import math
import query as qry
from urllib.parse import urlparse

tier = [5,10] # top 5: 3, top 10: 2, rest in google result: 1, not in google result: 0
N = 5

def strip_scheme(url):
# cited from https://stackoverflow.com/questions/21687408/how-to-remove-scheme-from-url-in-python
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)

def clean_url(url):
	ret = strip_scheme(url)
	return ret if ret[-1] != '/' else ret[:-1]

def google(keywords):
	response = GoogleSearch().search(keywords + "site:ics.uci.edu", num_results = 100, prefetch_pages = False)
	url = [result.url for result in response.results]
	url = list(map(clean_url, url))

	return [link for link in url if not link.endswith('.pdf')]

def dcg(gresults, myresults, perfect=False):
	scores = []
	for result in myresults:
		if result in gresults[:tier[0]]:
			scores.append(3)
		elif result in gresults[tier[0]:tier[1]]:
			scores.append(2)
		elif result in gresults[tier[1]:]:
			scores.append(1)
		else:
			scores.append(0)
	if perfect:
		scores.sort(reverse=True)
	discounted = [score/math.log2(i+1) if i != 0 else score for i,score in enumerate(scores)]
	print(discounted)
	return sum(discounted)

def ndcg(gresults, myresults):
	try:
		return dcg(gresults, myresults)/dcg(gresults, myresults, perfect=True)
	except ZeroDivisionError as e:
		return e
	

if __name__ == '__main__':
	query = ['mondego', 'machine learning', 'software engineering', 'security', 'student affairs', 'graduate courses', \
			'Crista Lopes', 'REST', 'computer games', 'information retrieval']
	se = qry.search_engine()
	for keywords in query:
		g = google(keywords)
		my = se.query(keywords)[0]
		print(g)
		print(my)
		print(keywords + ': ' + str(ndcg(g, my)))
