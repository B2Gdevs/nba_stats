#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 09:20:37 2018

@author: ben
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pickle


#testing
import nba_methods


def save_binary(path, obj):
    with open(path, 'wb') as file:
        pickle.dump(obj, file)
        
def load_binary(path):
    
    with open(path, 'rb') as file:
        obj = pickle.load(file)
    return obj

nba_stats = pd.read_csv('data.csv')
nba_stats = nba_stats.loc[:, 'data':]


unique_teams = nba_stats['opponent_names'].unique().tolist()


save_binary('unique_teams.pkl', unique_teams)
teams = load_binary('unique_teams.pkl')



# removing the final score and date.  just want quarters
    
nba_stats=nba_stats.drop(['date', 'final_score', 'opponent_points', 'diff_points'], axis=1)

nba_stats=pd.get_dummies(nba_stats)

nba_stats.loc[nba_stats['points'] <20, 'points'] = 1
nba_stats.loc[nba_stats['points'] >=20, 'points'] = 0

y_values = nba_stats['points']

nba_stats = nba_stats.drop('points', axis=1)

svm = SVC()


svm = svm.fit(nba_stats, y_values)


# save_binary('nba_svm_model.pkl', svm)
# save_binary('nba_X_training_data.pkl', nba_stats) 
# save_binary('nba_Y_training_data.pkl', y_values) 

# shortened_data = nba_stats.iloc[0:2,:]
# save_binary('shortened_X_data.pkl', shortened_data)


prediction = svm.predict(nba_stats)

print(classification_report(y_values, prediction))


# row = nba_methods.create_row('Houston Rockets','Portland Trail Blazers', 'OT', shortened_data)

# svm.predict([row])
