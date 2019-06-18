from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
#print(iris.target)
#print(iris.data)

X=np.array(iris.data)
y=np.array(iris.target)
#print(X.shape)
#print(y.shape)

#importing KNN library
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
#print(knn)
knn.fit(X, y)
print(knn.predict([[3,5,4,2]]))
print(knn.predict([[3,5,4,2],[5,4,3,2]]))

#use different neightbor value
knn = KNeighborsClassifier(n_neighbors=2)
#print(knn)
knn.fit(X, y)
print(knn.predict([[3,5,4,2]]))
print(knn.predict([[3,5,4,2],[5,4,3,2]]))

#import clssification model
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X,y)
print(logreg.predict([[3,5,4,2]]))
print(logreg.predict([[3,5,4,2],[5,4,3,2]]))
print(logreg.predict([[3,5,4,2],[5,4,3,2]]))
