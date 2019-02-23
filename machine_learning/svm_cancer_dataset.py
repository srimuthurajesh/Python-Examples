from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn import metrics

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

svm = SVC(kernel="linear")
svm.fit(X_train,y_train)
y_pred = svm.predict(X_test)

print(metrics.accuracy_score(y_test, y_pred))		#0.958041958041958
print(metrics.precision_score(y_test, y_pred))		#0.9883720930232558
print(metrics.recall_score(y_test, y_pred))			#0.9444444444444444


# The core idea of SVM is to find a maximum marginal hyperplane(MMH) that best divides the dataset into classes.

#Support Vectors -are data points, which are closest to the hyperplane.
#Hyperplane- decision plane which separates between a set of objects having different class memberships.
#Margin - a gap between the two lines on the closest class points.   i.e large margin - good margin, smaller margin-bad margin.

#HYPERPARAMETERS
#kernel trick: converts nonseparable problem to separable problems by adding more dimension to it. 
	#linear, polynomial, radial basis function (RBF) - Gaussian RBF, sigmoid, etc.

#Regularization: tells SVM optimization how much error is bearable. so we can custom margin
#Gamma

#DISADVANTAGES
#not suitable for large datasets, takes more time than Naïve Bayes. sensitive to type of kernel used
