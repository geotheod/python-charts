# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:56:24 2021

@author: geoth
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
from sklearn.preprocessing import LabelEncoder

filename = 'answers.csv'
df = pd.read_csv(filename, sep = ',',skiprows=[1,2])
#print(df)
#print(df[df.columns[3]].value_counts())
df = df.fillna(0)
print(df.columns[5])
answer = 1
for i in df.columns:
    print('i',i)
    print(df[i])    
    if any(isinstance(x, str) for x in df[i]):
        """
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(np.array(df[i]))
        print('Classes ', label_encoder.classes_)
        #print('Annotations ', label_encoder.__annotations__)
        print('integer encoded ',integer_encoded)
        print('Len integer encoded ',len(integer_encoded))
        inverted = label_encoder.inverse_transform(integer_encoded)      
        print('inverted ',inverted)
        print('continue')
        fig = plt.figure(figsize =(10, 7)) 
        plt.title("\n".join(wrap(i,60)), fontsize=14)
        
        # Creating plot 
        plt.boxplot(integer_encoded, patch_artist=True, 
                    boxprops=dict(facecolor='#0080fe', color='#0080fe'),
                    capprops=dict(color='black'),
                    whiskerprops=dict(color='green'),
                    #flierprops=dict(color='red', markeredgecolor='red'),
                    medianprops=dict(color='red',linestyle=None, linewidth=0), 
                    meanprops=dict(color='red', linewidth=2.5,linestyle='-'), 
                    showmeans=True, meanline=True) 
        plt.yticks(integer_encoded, inverted)
        plt.savefig(str(answer)+'-boxplot.png', bbox_inches='tight', dpi=300)
        # show plot 
        plt.show() 
        answer = answer + 1
        """
        continue
    fig = plt.figure(figsize =(10, 7)) 
    btitle = "\n".join(wrap(i,60))
    btitle = btitle + "\n"                   
    plt.title(btitle, fontsize=14)
    
    # Creating plot 
    plt.boxplot(df[i], patch_artist=True, 
                boxprops=dict(facecolor='#0080fe', color='#0080fe'),
                capprops=dict(color='black'),
                whiskerprops=dict(color='green'),
                #flierprops=dict(color='red', markeredgecolor='red'),
                medianprops=dict(color='red',linestyle=None, linewidth=0), 
                meanprops=dict(color='red', linewidth=2.5,linestyle='-'), 
                showmeans=True, meanline=True) 
    
    plt.savefig(str(answer)+'-boxplot.png', bbox_inches='tight', dpi=300)
    # show plot 
    plt.show() 
    answer = answer + 1
