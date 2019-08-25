from googleapiclient.discovery import build # news api requires js, can do that later
import newspaper 
import pprint
import config
import nltk
import time
import sys


class url_evaluator:
	# define variables and prepare article instance
	def __init__(self):
		self.a = newspaper.build_article(config.url)
		self.a.download()
		self.a.parse()
		self.a.nlp()
		
		self.hot = newspaper.hot()


	# get nouns from title
	def get_nouns_nltk(self):
		is_noun = lambda pos: pos[:2] == 'NN'
		tokenized = nltk.word_tokenize(self.a.title)
		nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

		return nouns
		

	# takes a search term, does a google search on it
	def google_search(self, search_term, **kwargs):
		try:
			service = build('customsearch', 'v1', developerKey=config.api_key)
			res = service.cse().list(q=search_term, cx=config.cse_id, **kwargs).execute()
		
			return res['items']

		except Exception as e:
			print('Google API returned error', e)
			sys.exit()
	

	# main of function
	def main(self):
		nouns = self.get_nouns_nltk()
		
		for i in nouns:
			results = self.google_search('i', num=10)

			for result in results:
				pprint.pprint(result)


if __name__ == '__main__':
	url_evaluator().main()
