# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:56:24 2021

@author: geoth
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
"""
fileinfo = {
        0: {'filename': 'base_kasteren.csv', 'separator': ' ', 'columns': ['date','time','attr1','attr2','state','concept:name']},
        1: {'filename': 'adlmr.csv', 'separator': ' ', 'columns': ['date','time','SensorId','Value','ResidentId','concept:name']},
        2: {'filename': 'activitylog_uci_detailed_labour.xes', 'separator': '', 'columns': []},
        3: {'filename': 'BPI_Challenge_2017.xes', 'separator': '', 'columns': []},
        
        }
"""

filename = 'answers.csv'
df = pd.read_csv(filename, sep = ',',skiprows=[1,2])
#print(df)
#print(df[df.columns[3]].value_counts())

answer = 1
for i in df.columns:
    y = df[i].value_counts()
    #plt.pie(y, labels = df[i].unique(),autopct='%1.1f%%')
    
    fig = plt.pie(y, autopct='%1.1f%%')
    
    plt.title("\n".join(wrap(i,60)), fontsize=14)
    labels = [ '\n'.join(wrap(str(l), 30)) for l in df[i].unique()]
    plt.legend(labels,bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
           bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    #plt.tight_layout()
    plt.savefig(str(answer)+'-piechart.png', bbox_inches='tight', dpi=300)
    plt.show()

    answer = answer + 1


"""
for i in df.columns:
    print(i)
    print(df[i])
    fig, ax = plt.figure(figsize=(16,8))
    # plot chart
    #ax1 = plt.subplot(121, aspect='equal')
    #df[i].plot(kind='bar', ax=axes[0], figsize=(10, 10), title='Population', alpha=0.5)
    df[i].plot(kind='pie', ax=ax, labels=i, fontsize=14)
    plt.show()
"""    

