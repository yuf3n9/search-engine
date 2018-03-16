import math
import query as qry
import json

tier = [5,10] # top 5: 3, top 10: 2, rest in google result: 1, not in google result: 0
N = 5

def clean_url(url):
	return url if url[-1] != '/' else url[:-1]

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
	with open('gresults.json', 'r') as f:
		d = json.loads(f.read())
	for keywords in query:
		g = d[keywords]
		my = list(map(clean_url, se.query(keywords)[0]))
		print(g)
		print(my)
		print(keywords + ': ' + str(ndcg(g, my)))
