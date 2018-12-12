from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
iris=datasets.load_iris()
X_train,X_test,Y_train,Y_test=train_test_split(iris.data,iris.target)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,Y_train)
model.score
metrics.accuracy_score(Y_test,model.predict(X_test))