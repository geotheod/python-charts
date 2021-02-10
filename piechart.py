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
    print('-----------------')
    print('df\n',df[i])
    y = df[i].value_counts()
    print('yb\n',y)
    y = y.sort_index()
    print('ya\n',y)
    print('yi\n',y.index)
    #plt.pie(y, labels = df[i].unique(),autopct='%1.1f%%')
    
    fig = plt.figure() 
    
    plt.pie(y, autopct='%1.1f%%')
    
    #plt.tight_layout()
    #axes.pie(textprops = dict(rotation_mode = 'anchor', va='center', ha='left'),)
    #fig.tight_layout()
    print('Length\n',str(i)+" "+str(len(i)))
    plt.title("\n".join(wrap(i,65)))
       
    #fig.update_layout(title_text=, title_x=0.5)
    labels = [ '\n'.join(wrap(str(l), 15)) for l in y.index]
    #labels.sort()

    
    plt.legend(labels,
               bbox_to_anchor=(1,0.5), 
               loc="center left", 
               fontsize=10,
               )#bbox_transform=plt.gcf().transFigure)
    
    #plt.gca().legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.legend(labels, loc="center")#, bbox_to_anchor=(0, 0), shadow=True, ncol=1) 
    #plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    #plt.tight_layout()
    plt.savefig(str(answer)+'-piechart.png', bbox_inches='tight', dpi=300)
    plt.show()

    answer = answer + 1
    print('-----------------')


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

