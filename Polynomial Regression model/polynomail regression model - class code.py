import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


dataset = pd.read_csv(r"C:\Users\Mukesh\OneDrive\Desktop\Tanmay Folder\emp-salary.csv")

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values



# Linear model -- linear algoritham (degree - 1)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)


plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x),color = 'blue')
plt.title('Linear regression model (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


lin_model_pred = lin_reg.predict([[6]])
lin_model_pred


lin_model_pred = lin_reg.predict([[7]])
lin_model_pred


# Polynomial Model -- degree-2
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures()
x_poly = poly_reg.fit_transform(x)


poly_reg.fit(x_poly, y)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)

plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)),color = 'blue')
plt.title('Polynomial regression model (Polynomail Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6]]))
poly_model_pred









