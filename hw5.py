from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NaN  

# Import data from hw5q1.xlsx
#frame = pd.read_excel('./hw5q1.xlsx')
#
## 1.a) boxplot data
#frame.boxplot()
#
## 1.b) 
#frame.applymap(lambda x: np.log2(x)).boxplot()
#
## 1.c)
#print(frame.describe(), "\n")
#
## 1.d)
#frame.hist(density = True)
#
## 1.e)
#frame.applymap(lambda x: np.log(x)).hist(density = True)
#
## 1.f)
#print("A: Normal Distribution\nB: Log Distribution\n" +
#      "C: Normal Distribution (Right-skewed)\nD: Log Distribution (Pareto)\n")


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
print("lol")

# print(frame.iloc[:5, 1:])
# list2 = [print(ele) for ele in frame.a if 4 > ele > 2]
# print(list2)
# print(frame.cumsum())
# print(frame.sum())
# print(frame.describe())
# print(frame.corr())

