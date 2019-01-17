from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()
X = iris.data
y = iris.target

#KNN N=1,31
n_range = range(1,31)
n_scores = []
"""for n in n_range:
	knn = KNeighborsClassifier(n_neighbors=n)	
	scores = cross_val_score(knn, X, y, cv=10 ,scoring='accuracy')
	n_scores.append(scores.mean())
print(n_scores) """

from sklearn.model_selection import GridSearchCV
param_grid = dict(n_neighbors=n_range)
knn = KNeighborsClassifier(n_neighbors=5)

#print(param_grid)		#{'n_neighbors': range(1, 31)}
grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy',return_train_score=False)
grid.fit(X, y)

#view result as panda dataframe
import pandas as pd
panDataFrame = pd.DataFrame(grid.cv_results_)[['mean_test_score','std_test_score','params']]
#print(panDataFrame.head())



import matplotlib.pyplot as plt
plt.plot(n_range,grid.cv_results_['mean_test_score'])
plt.xlabel('Value of N')
plt.ylabel('Accuracy')
plt.show()
		
	
