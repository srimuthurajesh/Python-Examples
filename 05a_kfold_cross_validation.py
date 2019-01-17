from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

iris = load_iris()
X = iris.data
y = iris.target

#KNN N=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10 ,scoring='accuracy')
print(scores.mean())


#KNN N=1,31
n_range = range(1,31)
n_scores = []
for n in n_range:
	knn = KNeighborsClassifier(n_neighbors=n)	
	scores = cross_val_score(knn, X, y, cv=10 ,scoring='accuracy')
	n_scores.append(scores.mean())
print(n_scores)

import matplotlib.pyplot as plt
plt.plot(n_range,n_scores)
plt.xlabel('Value of N')
plt.ylabel('Accuracy')
plt.show()
		
	
