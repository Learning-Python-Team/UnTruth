import urllib.request
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import newspaper

class title:

    #Initialisations
    def __init__(self):
        self.news_url="https://edition.cnn.com/2019/08/25/politics/trump-g7-boris-johnson-emmanuel-macron/index.html"
        self.net_con = True
        try:
            news_page=urllib.request.urlopen(self.news_url)
        
        except urllib.error.URLError:
            print("\nCONNECTIION ERROR:There may be a connection problem. Please check if the device is connected to the Internet")
            self.net_con=False


    def extract_headline(self):
        article = newspaper.Article(self.news_url)
        article.download()
        article.parse()
        return article.title.strip()

    #Adding Training Data
    def train_data(self, headline):
        try:
            with open('training_data.csv','r') as td:
                cl=NaiveBayesClassifier(td,format='csv')
                sentiment=cl.classify(headline)
                return sentiment

        except:
            print("\n\n Connection/Program Error")


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
