from googlesearch.googlesearch import GoogleSearch
# written by Anthony Hseb and modified to be compatible by notmikeb
import math

tier = [5,10] # top 5: 3, top 10: 2, rest in google result: 1, not in google result: 0
N = 5

def google(keywords):
	query = ['mondego', 'machine learning', 'software engineering', 'security', 'student affairs', 'graduate courses', \
			'Crista Lopes', 'REST', 'computer games', 'information retrieval']

	response = GoogleSearch().search(keywords + "site:ics.uci.edu", num_results = 100)
	url = [result.url for result in response.results]

	return url if url else []

def dcg(gresults, myresults):
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
	discounted = [score/math.log2(i+1) if i != 0 else score for score in scores]
	return sum(discounted)

def ndcg(gresults, myresults):
	return dcg(gresults, myresults)/dcg(gresults, myresults.sort(reverse=True))
