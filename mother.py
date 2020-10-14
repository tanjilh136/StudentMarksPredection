# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:11:07 2020

@author: USer Tanjil Hasan
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

from tkinter import *
import tkinter.font as tkFont

df=pd.read_csv('StudentsPerformance.csv')

def run():
    test_h = test_h_storage.get()
    test_parent = test_parent_storage.get()
    test_prerp = test_prerp_storage.get()
    
    XFeaturearray=df[['parental level of education','test preparation course','hour']].values
    YFeaturearray=df['AVG'].values

    #Model building  ====> 1
    model=LinearRegression();

    model.fit(XFeaturearray,YFeaturearray)

    print("Model Performances over Partens Level of Education: ")
    co_efficient_of_determination=model.score(XFeaturearray,YFeaturearray)
    print("co-efficient of determination of MODEL= ", co_efficient_of_determination)

    print("Intercept: ",model.intercept_)
    print("Slope: ",model.coef_)

    #Performing Prediction with the whole data
    YFeaturearray_predit=model.predict(XFeaturearray)
    print("predicted Mark (AVG) response with the whole DATA: ", YFeaturearray_predit);


    # Plot outputs
    #plt.scatter(XFeaturearray,YFeaturearray,color='black')
    plt.plot(XFeaturearray, YFeaturearray_predit, color='blue', linewidth=3)
    plt.xticks(())
    plt.yticks(())

    plt.show()

    plt.plot(XFeaturearray, YFeaturearray, color='black', linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()    

    test_par=test_parent.lower()
    test_pre=test_prerp.lower()
    if test_par=='ssc' or test_par=='school' or test_par=='high school':
      PLE=1
    elif test_par=='hsc' or test_par=='college':
      PLE=2
    elif test_par=='honors' or test_par=='bsc':
      PLE=3
    elif test_par=='master' or test_par=='masters' or test_par=='msc':
      PLE=4
    elif test_par=='phd' or test_par=='doctorate':
      PLE=5
    else:
      print('Wrong Entry')
      exit()

    if test_pre=='yes' or test_pre=='y':
      pre=1
    else:
      pre=0

    x_new=np.array([[PLE,pre,test_h]])
    y_new=model.predict(x_new)

    
    new_text = Label(text = y_new, fg = "green", bg = "white", font=fontStyle_result)
    new_text.place(x = 120, y = 460)


screen = Tk()
screen.title("Student Marks Predection")
screen.geometry("800x550")

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle_result = tkFont.Font(family="Lucida Grande", size=20)
welcome_text = Label(text = "Student Marks Predection", fg = "white", bg = "black", font=fontStyle)
welcome_text.pack()

test_h_text= Label(text = "Enter the amount of hours that you have read:")
test_h_text.place(x=120,y=80)

test_h_storage= DoubleVar()
test_h= Entry(textvariable = test_h_storage)
test_h.place(x=400,y=80)


test_parent_text= Label(text = "Choose your parents level of education")
test_parent_text.place(x=120,y=120)


test_parent_storage= StringVar()
test_parent= Entry(textvariable = test_parent_storage)
test_parent.place(x=400,y=120)

test_parent_text1= Label(text = "\t\tSSC/high School/ School \n\t\tHSC/college\n\t\tHonors/BSC\n\t\tMasters\n\t\tPhd/Doctorate\n")
test_parent_text1.place(x=500,y=110)

test_prerp_text = Label(text = "Have you taken your preparation: ")
test_prerp_text.place(x=120,y=200)


test_prerp_storage = StringVar()
test_prerp = Entry(textvariable = test_prerp_storage)
test_prerp.place(x=400,y=200)

test_prerp_text1 = Label(text = "\t\tYes\n\t\tNo\n")
test_prerp_text1.place(x=500,y=200)


click = Button(text = "Predict Marks", fg = "blue", bg = "grey", command = run)
click.place(x=400, y=360)

mainloop()
