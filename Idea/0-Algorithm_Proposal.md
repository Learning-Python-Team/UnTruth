# Proposing Algorithm

The critical thinking model applied on humans can also be applied to a program in order to write an algorithm that detects a fake news. The program can be written in several parts ensuring that each module carry out only a single step from the steps below.

##### Critical Thinking Model:

1. Read the headline.
2. Read the entire article.
3. Don’t believe a word of anything you read until you check facts and check sources.
4. Are the sources and facts credible? Why or why not?
5. Do a quick search engine scan to see who else has covered the story.
6. Do you see two sides (or more) to the article?
7. Are you being spun? Do you feel manipulated?
8. Are other credible news outlets covering the story?
9. Is this story a potential fake news story?


### Implementation


#### Read the headline
The headline will provide the program a rough idea. It may be designed in a way that the headline will be reverse-searched on top search engines and gather all the data from similar headlines into heap. The program will also look up for the data on the source website to estimate the legitness_score of that source.



#### Read the entire article
The next steps involves scanning through the whole article word by word and finding relevant patterns that may be crucial to further classify the article into fake or legit. Further the motive of the article may be compared with the headline to predict weather the misleading_title returns True or False



#### Don’t believe a word of anything you read until you check facts and check sources
The initial overall trust_score of the article always always remains -1 until all the scores are calculated i.e The program will always consider the news to be fake unless it had completely processed it, hence not giving any preference to BBC.com over FakeNews.com and both considered a fake initially



#### Are the sources and facts credible? Why or why not?
The source of the current article, the author and the images on the article are reverse-searched to ensure the credibility of the source. the history of posts from the same author and images uploaded on the article are original or just carried forward from other sources and articles



#### Do a quick search engine scan to see who else has covered the story. *


#### Do you see two sides (or more) to the article?
This step may involve checking if the article is comparing one entity with another example, political parties. The job of the program here is to determine what is being talked about here and what is it compared with eg: An article constantly comparing Males and Females



#### Are you being spun? Do you feel manipulated?
The next part will help determine if the article is biased towards one side more than the other, in the above example if the article is about Males and Females, the program checks if there's any bias to the comparison, One being favoured more over other and calculate the bias_score . When in favour of females the bias_score for females will be shown as +1 and -1 for men. unbias will be reflected with a bias_score totalling to 0



#### Are other credible news outlets covering the story?


#### Is this story a potential fake news story?
Finally after everything is taken into consideration, The parameters will be used to label the data to be a fake or a legit



