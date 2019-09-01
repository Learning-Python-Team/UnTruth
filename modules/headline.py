import newspaper
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import urllib.request
import sys


class title:
	#Initialisations
	def __init__(self): 
		self.news_url=input("\nEnter The URL : ")
		self.pos=[] #Variable to store all positive tokens from positive_headlines.csv file
		self.neg=[] #Variable to store all negative tokens from negative_headlines.csv file
		
		try:
			self.news_page=urllib.request.urlopen(self.news_url)
		
		except urllib.error.URLError:
			print("\nCONNECTIION ERROR:There may be a connection problem. Please check if the device is connected to the Internet")
			sys.exit()

	# extract headline
	def extract_headline(self):
		try:
			article = newspaper.Article(self.news_url)
			article.download()
			article.parse()
			return article.title.strip()
		except newspaper.article.ArticleException: #List possible errors in case of any exception
			print("\nCONNECTION/URL ERROR: Article could not be retrieved.")

			
	#Adding Training/Testing Data
	def train(self,headline):
		with open("positive_headlines.csv") as file:
			for sentence in file:
				self.pos.append([{word: True for word in nltk.word_tokenize(sentence)},'Positive'])

		with open("negative_headlines.csv") as file:
			for sentence in file:
				self.neg.append([{word: True for word in nltk.word_tokenize(sentence)},'Negative'])

		training=self.pos[:int(len(self.pos))] + self.neg[:int(len(self.neg))]

		classifier = NaiveBayesClassifier.train(training) #Training
		sentiment=classifier.classify({word: True for word in nltk.word_tokenize(headline)})
		return sentiment

	# categorize headline
	def headline_category(self,headline,sentiment):
		print("\nHEADLINE  :",headline.upper())
		print("SENTIMENT :",sentiment)
		print("AUTHOR(S) :",*self.article.authors,'\n')

		
	# main of class
	def main(self):
		hdln=self.extract_headline()
		sntmnt=self.train(hdln)
		self.train(hdln)
		self.headline_category(hdln,sntmnt)
		
		
if __name__=='__main__':
	title().main()
	