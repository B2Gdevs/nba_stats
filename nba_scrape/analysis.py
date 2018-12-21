#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 09:20:37 2018

@author: ben
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

nba_stats = pd.read_csv('data.csv')
nba_stats = nba_stats.loc[:, 'data':]


unique_teams = nba_stats['opponent_names'].unique()
# =============================================================================
# count = 0
# 
# for team in unique_teams:
#     nba_stats.loc[nba_stats['opponent_names'] == team, ['opponent_names']]\
#                   = count
#                   
#     nba_stats.loc[nba_stats['team_names'] == team, ['team_names']]\
#                   = count
#                   
#     count+=1
# =============================================================================
    
# removing the final score and date.  just want quarters
    
nba_stats=nba_stats.drop(['date', 'final_score'], axis=1)

nba_stats=pd.get_dummies(nba_stats)
