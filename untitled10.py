print("Name : Oga")

#import the libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Task 1
#Read the BMI.csv
bmi_df = pd.read_csv('BMI.csv')
print(bmi_df)

#Task 2
#Data is sorted in descending order in accordance with BMI value
#Find the top 5 age group where the BMI value is the highest, and plot a bar graph out of it
bmi_top_5 = bmi_df.head(5)
name = bmi_top_5['Age']
number = bmi_top_5['BMI']

plt.ylabel("BMI")
plt.xlabel("Age")
plt.xticks(rotation = 'vertical')

plt.bar(name, number, width = 0.4, color = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'))

#Task 3
#Read blood_pressure.csv
bp_df = pd.read_csv('BP.csv')
print(bp_df)

#Task 4
#Data is sorted in ascending order in accordance with Blood Pressure
#Find the top 5 age group where the BloodPressure value is the highest, and plot a bar graph out of it
bp_top_5 = bp_df.tail(5)
name = bp_top_5['Age']
number = bp_top_5['BMI']

plt.ylabel("Blood Pressure")
plt.xlabel("Age")
plt.xticks(rotation = 'vertical')

plt.bar(name, number, width = 0.4, color = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'))

#Task 5
#Read the insulin.csv
insulin_df = pd.read_csv('Insulin.csv')
print(insulin_df)

#Task 6
#Data is sorted in descending order in accordance with Insulin value
#Find out what will be the Glucose and BMI value when the Insulin is highest
top_1 = insulin_df.head(1)
print(top_1)

print("When Insulin is the highest, Glucose is : ", top_1['Glucose'])
print("When Insulin is the highest, BMI Value is : ", top_1['BMI'])
