import newspaper    
def citation_check(article_object):
    
    #Something NLTK stop words. These often aren't real citations. / to remove local files, and ad removal from scraped link.
    not_citations = ("facebook.com", "twitter.com", "#", "mailto", "plus.google", "advertising", "advertisement", "ad.", "/", "whatsapp")

    article_html = article_object.html
    http = [article_object.url] + re.findall(r'href="[^\"]+', article_html) #Regex code for finding links, eg href="http://www.bbc.com" returns http://www.bbc.com.
    unique_citations = [] #Initialize unique urls to null.

    #Find all cleaned urls (without http, https or www)
    for http_url in http:
        #Convert https to http, convert www to null, convert \ to /, and convert href to null
        http_url = http_url.replace('https', 'http').replace('www.', '').replace('\\', '/').replace('href="','')
        #Split string into two - http:// part and following URL part, then split again using  and use the 0th element to get the general source.
        splitted = http_url.split("http://")[-1].split("/")
        if splitted[0].strip().startswith(not_citations) is False and splitted[0].strip() not in unique_citations:
            unique_citations.append(splitted[0])
    
    #split_http stores all the unique websites/citations that the article webpage has linked to.
    
    number_unique_citations = len(unique_citations) - 1  #Unique citations = Length of all unique website links minus itself

    return number_unique_citations

#For prototyping only - 
if(__name__=="__main__"):
    article = newspaper.Article("http://www.bbc.com/future/story/20190801-tomorrows-gods-what-is-the-future-of-religion")
    article.download()
    article.parse()
    print(citation_check(article))
