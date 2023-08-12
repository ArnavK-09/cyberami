# imports 
from __future__ import annotations
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# log 
log = print

# start 
log("[Model] Started Processing Data...")

data: pd.DataFrame = pd.read_csv("data/main.csv")
data["Label"] = data["Label"].map({"bad": 0, "good": 1})
X: pd.Series = data["URL"]
Y: pd.Series = data["Label"]
model: Pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', LogisticRegression(solver='lbfgs', max_iter=1000000))
])
model.fit(X, Y)

# end 
log("[Model] Started Processing Data...")

# model dump 
pickle.dump(model,open('model.pkl','wb'))