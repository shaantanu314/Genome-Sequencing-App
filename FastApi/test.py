# Importing Necessary modules
from fastapi import FastAPI, UploadFile, File
import uvicorn
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from pydantic import BaseModel
 
# Declaring our FastAPI instance
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}
 


@app.post('/predict')
async def predict_species(Index : int, model: int = None, steps: int = None):


    import numpy as np # linear algebra
    import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    import os
    import matplotlib.pyplot as plt
    import json

    # contents = await file.read()
    # file_text = contents.decode("utf-8")
    human_dna = pd.read_table('human.txt')
    human_dna.head()
    if(Index == 0):
        chimp_dna = pd.read_table('chimpanzee.txt')
    elif(Index == 1):
        chimp_dna = pd.read_table('dog.txt')
    else:
        return {"error" : "Invalid Input"}
    chimp_dna.head()

    def Kmers_funct(seq, size=6):
        return [seq[x:x+size].lower() for x in range(len(seq) - size + 1)]

    human_dna['words'] = human_dna.apply(lambda x: Kmers_funct(x['sequence']), axis=1)
    human_dna = human_dna.drop('sequence', axis=1)

    chimp_dna['words'] = chimp_dna.apply(lambda x: Kmers_funct(x['sequence']), axis=1)
    chimp_dna = chimp_dna.drop('sequence', axis=1)

    human_texts = list(human_dna['words'])
    for item in range(len(human_texts)):
        human_texts[item] = ' '.join(human_texts[item])
    #separate labels
    y_human = human_dna.iloc[:, 0].values # y_human for human_dna

    chimp_texts = list(chimp_dna['words'])
    for item in range(len(chimp_texts)):
        chimp_texts[item] = ' '.join(chimp_texts[item])
    #separate labels
    y_chim = chimp_dna.iloc[:, 0].values # y_chim for chimp_dna

    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(4,4)) #The n-gram size of 4 is previously determined by testing
    X = cv.fit_transform(human_texts)
    X_chimp = cv.transform(chimp_texts)
    print(X.shape)
    print(X_chimp.shape)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y_human, 
                                                        test_size = 0.20, 
                                                        random_state=42)

    from sklearn.naive_bayes import MultinomialNB
    classifier = MultinomialNB(alpha=0.1)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
    print("Confusion matrix for predictions on human test DNA sequence\n")
    print(pd.crosstab(pd.Series(y_test, name='Actual'), pd.Series(y_pred, name='Predicted')))
    def get_metrics(y_test, y_predicted):
        accuracy = accuracy_score(y_test, y_predicted)
        precision = precision_score(y_test, y_predicted, average='weighted')
        recall = recall_score(y_test, y_predicted, average='weighted')
        f1 = f1_score(y_test, y_predicted, average='weighted')
        return accuracy, precision, recall, f1
    accuracy, precision, recall, f1 = get_metrics(y_test, y_pred)
    print("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f" % (accuracy, precision, recall, f1))

    y_pred_chimp = classifier.predict(X_chimp)

    print("Confusion matrix for predictions on Chimpanzee test DNA sequence\n")
    print(pd.crosstab(pd.Series(y_chim, name='Actual'), pd.Series(y_pred_chimp, name='Predicted')))
    accuracy, precision, recall, f1 = get_metrics(y_chim, y_pred_chimp)
    print("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f" % (accuracy, precision, recall, f1))
    stat = {
        "acc"   : accuracy,
        "prec"  : precision,
        "rec"   : recall,
        "f1"    : f1
        }
    output = json.dumps(stat)
    print(output)
    return {"acc"   : accuracy,
        "prec"  : precision,
        "rec"   : recall,
        "f1"    : f1,
        }
