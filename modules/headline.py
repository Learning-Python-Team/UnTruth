import urllib.request
from bs4 import BeautifulSoup
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import newspaper
import nltk

class title:

    #Initialisations
    def __init__(self): 
        self.news_url="https://edition.cnn.com/2019/08/25/politics/trump-g7-boris-johnson-emmanuel-macron/index.html"


    def extract_headline(self):
        self.net_con=True #Expecting Internet Connection to be working initially
        
        try:
            article = newspaper.Article(self.news_url)
            article.download()
            article.parse()
        
        except urllib.error.URLError:
            print("\nCONNECTIION ERROR:There may be a connection problem. Please check if the device is connected to the Internet")
            self.net_con=False #Value update if the program is unable to connenct
            article.title = "Invalid URL/Could not extract title"
        return article.title.strip()



    #Adding Training Data
    def train_data(self, headline):
        try:
            with open('training_data.csv','r') as td:
                cl=NaiveBayesClassifier(td,format='csv')
                sentiment=cl.classify(headline)
                return sentiment

        except:
            if self.net_con==False:
                pass
            else:
                print("\n\nProgram Error")


    def headline_category(self,headline,sentiment):

        analyse_headline=TextBlob(headline)
        print("\n"+"Headline:",headline,"\n")
        print("Headline Sentiment:",sentiment,"\n\n")

    def main(self):
        hdln=self.extract_headline()
        sntmnt=self.train_data(hdln)
        self.headline_category(hdln,sntmnt)

if __name__=='__main__':
    do_ya_thing=title()
    do_ya_thing.main()
