#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:06:44 2019

@author: ben
"""

import pandas as pd
import numpy as np
import pickle 

def create_row(team, opposing_team, quarter, dataframe):
    
    opponent_column = 'opponent_names_' + opposing_team
    team_column = 'team_names_' + team
    # quarter names are 1st, 2nd, 3rd, 4th, OT, 2OT, 3OT, 4OT
    quarter_column = 'quarters_' + quarter

    columns = dataframe.columns
    row = []
    
    for column in columns:
        if column == opponent_column:
            row.append(1)
        elif column == team_column:
            row.append(1)
        elif column == quarter_column:
            row.append(1)
        else:
            row.append(0)
            
    return row


def save_binary(path, obj):
    with open(path, 'wb') as file:
        pickle.dump(obj, file)
        
def load_binary(path):
    
    with open(path, 'rb') as file:
        obj = pickle.load(file)
    return obj
    
    