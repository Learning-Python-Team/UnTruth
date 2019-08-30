import newspaper
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

class title:
    #Initialisations


    def __init__(self): 
        self.news_url=input("\nEnter The URL : ")
        self.pos=[] #Variable to store all positive tokens from positive_headlines.csv file
        self.neg=[] #Variable to store all negative tokens from negative_headlines.csv file


    def extract_headline(self):

        try:
            self.article = newspaper.Article(self.news_url)
            self.article.download()
            self.article.parse()
        
        except newspaper.article.ArticleException: #List possible errors in case of any exception
            print("\nCONNECTION/URL ERROR: There may be a problem with your connection or the URL entered may be invalid")
            article.title = "Invalid URL/Could not extract title"

        return self.article.title.strip()


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


    def headline_category(self,headline,sentiment):
        print("\nHEADLINE  :",headline.upper())
        print("SENTIMENT :",sentiment)
        print("AUTHOR(S) :",*self.article.authors,'\n')


    def main(self):
        hdln=self.extract_headline()
        sntmnt=self.train(hdln)
        self.train(hdln)
        self.headline_category(hdln,sntmnt)
        
        
if __name__=='__main__':
    do_ya_thing=title()
    do_ya_thing.main()