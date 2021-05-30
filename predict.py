


import joblib
import numpy as np


model = joblib.load('marks.pk2')


no_of_students=int(input("how many students marks you want to predict : "))
for i in range(no_of_students):
    hour=input("how much hours do you study? :")
    hour_int=float(hour)# to convert it into float type because "input" return string
    type(hour_int)
    marks=model.predict([[hour_int]])# this cmd take only int or float
    marks_final=float(marks)
    print(f"you predicted marks is {marks_final}")





