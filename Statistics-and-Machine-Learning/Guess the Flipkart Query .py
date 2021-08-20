import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC, LinearSVC

f=open('training.txt')
file=f.readlines()
n=int(file[0])
X,y=[],[]
for lines in file[1:]:
    if lines.__contains__(")"):
        index = lines.index(")")
        X.append(lines[:index+1].strip())
        y.append(lines[index+1:].strip())
X=np.array(X)
y=np.array(y)
model= Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', LinearSVC())])
model.fit(X,y)
X_test=[]
n=int(input())
for z in range(n):
    X_test.append(input())
    for val in model.predict(X_test):
            print(val)
            X_test =[]