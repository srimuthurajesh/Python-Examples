from sklearn.datasets import load_iris

iris = load_iris()
X=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=60,random_state=4)
#test_size=0.4 if it is given in percentage as 40%
#if nothing is provided, default value is 25%(0.25)

#print(X_train.shape)	#90,4
#print(y_train.shape)	#90,4
#print(X_test.shape)		#60
#print(y_test.shape)		#60

#Logistic Regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test,y_pred))			#0.9333333333 accuracy


#KNN  N=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred))			#0.9666666666666667 accuracy

#KNN  N=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred))			#0.95 accuracy
	

n_range = list(range(1,26))
accuracy_level=[]
for n in n_range:
	knn = KNeighborsClassifier(n_neighbors=n)
	knn.fit(X_train,y_train)
	y_pred=knn.predict(X_test)
	accuracy_level.append(metrics.accuracy_score(y_test,y_pred))
	
#Gonna make a plot graph
import matplotlib.pyplot as plt
plt.plot(n_range,accuracy_level)
plt.title('KNN(N-value) vs Accuracy')
plt.xlabel('Value of n for KNN')
plt.ylabel('Accurracy in %')	
plt.grid(True,color='k')
plt.show()


#based on graph plot 11 has high accuracy
#SOLUTION:
knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X, y)
knn.predict([[3, 5, 4, 2]])
