import nltk
import newspaper
import re

class article_content():

    def __init__(self, article_object):
        #Whenever a class object is made, the article is tokenized and the dictionary file is opened as a set.
        self.tokenized_words = nltk.word_tokenize(article_object.text)
        self.article_object = article_object
        with open('words_alpha.txt') as word_file:
            self.valid_words = set(word_file.read().split())
        
        self.misspells = 0  # Set initial misspells to 0.

    def citation_check(self):
        
        #Something NLTK stop words. These often aren't real citations. / to remove local files, and ad removal from scraped link.
        self.not_citations = ("facebook.com", "twitter.com", "#", "mailto", "plus.google", "advertising", "advertisement", "ad.", "/", "whatsapp", "quora", "nav.", "instagram")

        self.article_html = self.article_object.html
        http = [self.article_object.url] + re.findall(r'href="[^\"]+', self.article_html) #Regex code for finding links, eg href="http://www.bbc.com" returns http://www.bbc.com.
        self.unique_citations = [] #Initialize unique urls to null.

        #Find all cleaned urls (without http, https or www)
        for http_url in http:
            #Convert https to http, convert www to null, convert \ to /, and convert href to null
            http_url = http_url.replace('https', 'http').replace('www.', '').replace('\\', '/').replace('href="','')
            #Split string into two - http:// part and following URL part, then split again using  and use the 0th element to get the general source.
            splitted = http_url.split("http://")[-1].split("/")
            if splitted[0].strip().startswith(self.not_citations) is False and splitted[0].strip() not in self.unique_citations:
                self.unique_citations.append(splitted[0])
        
        #split_http stores all the unique websites/citations that the article webpage has linked to.
        
        self.number_unique_citations = len(self.unique_citations) - 1  #Unique citations = Length of all unique website links minus itself

        return self.number_unique_citations

    def spell_check(self):
        for word in self.tokenized_words: #For every word in article
            if word[0].isupper()==False: #Ignore if first letter is uppercase, else
                word_lowercase = word.lower() #Convert to lowercase
                asciis = [ord(char) for char in word_lowercase] #Find out ASCIIs of word

                if all(ascii_key >= 97 and ascii_key <= 122 for ascii_key in asciis)==True: #Only accept is ASCII's are alphabetical. Numbers cannot be misspelled.
                    if word_lowercase not in self.valid_words and len(word_lowercase)>1: #Check if greater than 1 length and not in dictionary
                        self.misspells +=1 
        
        return self.misspells
        

#For prototyping only - 
if(__name__=="__main__"):
    article = newspaper.Article("http://www.bbc.com/future/story/20190801-tomorrows-gods-what-is-the-future-of-religion")
    article.download()
    article.parse()
    ArtCon = article_content(article)  #Create object. This opens init and tokenizes article.
    print("Number of citiations, ", ArtCon.citation_check())  #Citation check
    print("Number of misspells, ", ArtCon.spell_check()) #Spell check
