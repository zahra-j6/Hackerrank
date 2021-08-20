from nltk import sent_tokenize
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

file=open('apple-fruit.txt',encoding='UTF-8')
apple=file.readlines()
file=open('apple-computers.txt',encoding='UTF-8')
inc=file.readlines()
type, text=[],[]

for line in apple[22:]:
    sentences=sent_tokenize(line)
    for word in sentences:
        text.append(word)
        type.append("fruit")

for line in inc[43:]:
    sentences=sent_tokenize(line)
    for word in sentences:
        text.append(word)
        type.append("computer-company")
df=pd.DataFrame(zip(text,type),columns=["Text","Type"]);
model = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier())])
model.fit(text,type)
n=int (input())
X_test=[]
for z in range(n):
    X_test.append(input())
    for val in model.predict(X_test):
            print(val)
            X_test =[]