from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "hello how are you",
    "let's meet tomorrow",
    "win money now",
    "free prize claim",
    "claim your reward",
    "how is your day"
]

labels = [0, 0, 1, 1, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict(text):
    X_input = vectorizer.transform([text])
    return model.predict(X_input)[0]