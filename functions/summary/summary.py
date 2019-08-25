# rewritten from https://github.com/edubey/text-summarizer/blob/master/text-summarizer.py

from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords
import numpy as np
import newspaper
import config
import networkx as nx


class summarizer:
	# define variables
	def __init__(self):
		self.a = newspaper.build_article(config.url)
		self.a.download()
		self.a.parse()
		self.a.nlp()
		
		self.hot = newspaper.hot()


	# get sentences from article main
	def text_to_sentences(self):
		sentences = list()
		
		article = self.a.text
		article = article.replace('\n\n', '. ')
		article_sentences = article.split(r'. ')

		for sentence in article_sentences:
			sentences.append(sentence.replace('[^a-zA-Z]', '').split(' '))

		return sentences


	# determines sentence similarity
	def sentence_similarity(self, sent1, sent2, stopwords=None):
		if stopwords is None:
			stopwords = []
	
		sent1 = [w.lower() for w in sent1]
		sent2 = [w.lower() for w in sent2]
	
		all_words = list(set(sent1 + sent2))
	
		vector1 = [0] * len(all_words)
		vector2 = [0] * len(all_words)
	
		for w in sent1:
			if w in stopwords:
				continue
			vector1[all_words.index(w)] += 1
	
		for w in sent2:
			if w in stopwords:
				continue
			vector2[all_words.index(w)] += 1
	
		return 1 - cosine_distance(vector1, vector2)


	# takes article content, returns key words
	def build_similarity_matrix(self, content, stop_words, sentences):
		similarity_matrix = np.zeros((len(sentences), len(sentences)))
	
		for idx1 in range(len(sentences)):
			for idx2 in range(len(sentences)):
				if idx1 == idx2: 
					continue 
				similarity_matrix[idx1][idx2] = self.sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

		return similarity_matrix


	# main of function
	def main(self):
		summarize_text = list()

		sentences = self.text_to_sentences()

		sentence_similarity_matrix = self.build_similarity_matrix(self.a.text, stopwords.words('english'), sentences)
		
		sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
		scores = nx.pagerank(sentence_similarity_graph)

		ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    

		for i in range(config.lines):
			summarize_text.append(" ".join(ranked_sentence[i][1]))

		return summarize_text


if __name__ == '__main__':
	print("Summarized Text: \n", ". ".join(summarizer().main()))
