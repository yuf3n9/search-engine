from googlesearch.googlesearch import GoogleSearch
# written by Anthony Hseb and made compatible to py3 by notmikeb
# add more delay by myself to avoid request denial
from urllib.parse import urlparse
import json

def strip_scheme(url):
# cited from https://stackoverflow.com/questions/21687408/how-to-remove-scheme-from-url-in-python
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)

def clean_url(url):
	ret = strip_scheme(url)
	return ret if ret[-1] != '/' else ret[:-1]

def google(keywords):
	response = GoogleSearch().search(keywords + " site:ics.uci.edu", num_results = 100, prefetch_pages = False)
	url = [result.url for result in response.results]
	url = list(map(clean_url, url))

	return [link for link in url if not link.endswith('.pdf')]

if __name__ == '__main__':
	query = ['mondego', 'machine learning', 'software engineering', 'security', 'student affairs', 'graduate courses', \
			'Crista Lopes', 'REST', 'computer games', 'information retrieval']
	d={}
	for keywords in query:
		d[keywords] = google(keywords)
		with open('gresults.json', 'w') as f:
			f.write(json.dumps(d))