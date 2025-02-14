from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import nan as NaN  

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2

# Import data from hw5q1.xlsx
frame = pd.read_excel('./hw5q1.xlsx')

# 1.a) boxplot data
frame.boxplot()
plt.show()

# 1.b) 
frame.applymap(lambda x: np.log2(x)).boxplot()
plt.show()

# 1.c)
print(frame.describe(), "\n")

# 1.d)
frame.hist(density = True)
plt.show()

# 1.e)
frame.applymap(lambda x: np.log(x)).hist(density = True)
plt.show()

# 1.f)
print("A: Normal Distribution\n" +
      "C: Log Normal Distribution\n")


# 2.a) Import data from brfss.csv
frame2 = pd.read_csv('./brfss.csv')
frame2.name = 'brfss' # Rename DataFrame
frame2 = frame2.drop(['wtyrago', 'wtkg2'], axis = 1) # drop columns
frame2.sex = frame2.sex.apply(lambda x: 0 if x == 2 else 1) # Set Sex
frame2 = frame2.rename(columns={'Unnamed: 0': 'index','weight2': 'weight', 
                                'htm3': 'height', 'sex': 'male'})
frame2_wNull = frame2
frame2 = frame2.dropna() # Drop NULL

# 2.b.i) Max age in DataSet
print("Max age:\n", frame2.age.max(), "\n")

# 2.b.ii) Mean weight in DataSet
print("Mean weight:\n", frame2.weight.mean(), "kg", "\n")

# 2.b.iii) Mean weight for male in DataSet
male = frame2.male == 1
meanMale = frame2[male & frame2.weight]
print("Mean Male weight:\n", meanMale.weight.mean(), "kg", "\n")

# 2.b.iv) Median height for female in DataSet
female = frame2.male == 0
medianFemale = frame2[female & frame2.weight]
print("Median Female height:\n", medianFemale.height.median(), "cm", "\n")

# 2.b.v) Mean weight for female younger than 20 years old
female = frame2.male == 0
under20 = frame2.age < 20
meanFemale = frame2[female & under20]
print("Mean Female under 20 weight:\n", meanFemale.weight.mean(), "kg", "\n")

# 2.b.vi) # of Males in dataset
male = frame2.male == 1
print("Count of Males in DataFrame:\n", male.sum(), "\n")

# 2.b.vii) # Height > 190cm & Weight < 50 kg
tall = frame2.height > 190
thin = frame2.weight < 50
tallThin = frame2[thin & tall]
print("Count of Height > 190cm & Weight < 50kg:\n", len(tallThin.index), "\n")

# 2.b.viii) # average height females, weight between 59 and 61 kg
greaterThan59 = frame2.weight > 59
lessThan61 = frame2.weight < 61
female = frame2.male == 0
female59_61 = frame2[female & greaterThan59 & lessThan61]
print("Avg height Female weight between 59 - 61kg:\n", 
      female59_61.height.mean(), "\n")

# 2.b.ix) # Print rows 2001 to row 2010 (inclusive)
print("Print Rows 2001 - 2010 (inclusive):\n", 
      frame2_wNull[2001: 2011], "\n")

# 2.b.x) # Print Rows 2001 - 2010 (inclusive, drop rows w/ NULL entries)
print("Print Rows 2001 - 2010 (inclusive, drop rows w/ NULL entries):\n", 
      frame2_wNull[2001: 2011].dropna(), "\n")

# 3.a) 
lr = linear_model.LinearRegression()
x = pd.DataFrame(frame2.weight)
y = frame2.height

lr.fit(x, y)
pred = lr.predict(x)

# lr.coef_ = beta, lr.intercept = alpha
print('height = %.2f * weight + %.2f' %(lr.coef_, lr.intercept_))


# 3.b) predict height of individual whose weight is 60 kg
print('predicted height when weight is 60kg: %.2f\n' %(lr.predict(60)))
      
# 3.c) Calculate MSE and R2
print('mse = %.2f' %mse(y, pred))
print('r2 = %.2f\n' %r2(y, pred))

# 3.d) 
y = frame2.height
x = frame2[['weight','male']]
lr = linear_model.LinearRegression()
lr.fit(x, y)

print(lr.coef_)

#coef = Series(lr.coef_, index = list(frame2.columns))
# print(coef)