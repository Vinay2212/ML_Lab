from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
doc= fetch_20newsgroups_vectorized()
model=MultinomialNB()
X_train,X_test,Y_train,Y_test=train_test_split(doc.data,doc.target)
model.fit(X_train,Y_train)
print("Accuracy:")
print(metrics.accuracy_score(Y_test,model.predict(X_test)))
print("Precision:")
print(metrics.precision_score(Y_test,model.predict(X_test),average=None))
print("Recall:")
print(metrics.recall_score(Y_test,model.predict(X_test),average=None))