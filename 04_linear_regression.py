import pandas as pd
data = pd.read_csv('sales.csv', index_col=0)
#print(data.head())		#columns: 'TV','Radio','Newspaper','Sales'

X = data[['TV','Radio','Newspaper']]
y = data['Sales']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)		#test_size default 25%
#print(X_train.shape)		#(150, 3)
#print(y_train.shape)		#(150,)
#print(X_test.shape)		#(50, 3)
#print(y_test.shape)		#(50,)


from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train,y_train)
y_pred = linreg.predict(X_test)
print(y_pred)


"""LINEAR REGRESSION EXPLANATION
	response = intercept + B1x1 + B2x2 +.......+Bnxn
		where B1,B2,B3 are model coefficients	"""
#print(linreg.intercept_)		#return intercept
#print(linreg.coef_)			#return array of coefficent for the column features		

""" THERE TYPE OF EVAULATION MATRIX
	1.Mean absolute error		-metrics.mean_absolute_error(true, pred)
	2.Mean squared error		-metrics.mean_squared_error(true, pred)
	3.Root mean squared error	-metrics.mean_squared_error(true, pred)	
"""


from sklearn import metrics
print(metrics.mean_squared_error(y_test,y_pred))		
