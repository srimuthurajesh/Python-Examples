from sklearn.datasets import load_iris

iris = load_iris()
#print(iris.target)
#print(iris.data)
X=iris.data
y=iris.target
#print(X.shape)
#print(y.shape)

#Logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, y)
#predict for entire dataset
y_pred = logreg.predict(X)

#import metrics to calculat accuracy
from sklearn import metrics
print(metrics.accuracy_score(y,y_pred))			#0.96 accuracy

#KNN k=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
y_pred = knn.predict(X)
print(metrics.accuracy_score(y, y_pred))		#0.9666666666666667 accuracy
	
#KNN k=1
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
y_pred = knn.predict(X)
print(metrics.accuracy_score(y, y_pred))		#1.0 accuracy
		
