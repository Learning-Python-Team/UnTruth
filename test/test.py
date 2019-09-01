def train_classifier(self,headline):

    a=input("""\nIf you think the output was incorrect, Please re-label the headline's sentiment to train the classifier 
     & help improve future predictions [p/n]: """)

    if a=='p':
        with open('positive_headlines.csv','a') as td:
                td.write('\n'+headline)
    elif a=='n':
        with open('negative_headlines.csv','a') as td:
                td.write('\n'+headline)
    else:
        print("Incorrect key pressed!")
    pass

self.train_classifier(hdln)