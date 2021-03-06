# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:52:07 2021

@author: geoth
"""

# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from textwrap import wrap
 
filename = 'answers.csv'
df = pd.read_csv(filename, sep = ',',skiprows=[1,2])
df = df.fillna(0)
print(df.columns[5])
answer = 1
for i in df.columns:
    
    print('i',i)
    print(df[i])
    y = df[i]
    if any(isinstance(x, str) for x in y):
        print("the list contains a string")
        y = y.astype(str)    
    
    y = y.value_counts()

    y = y.sort_index()
    print('y\n',y)

    stats = y
    print('stats\n',stats)
    labels = y.index
    print('labels',labels)
    stats = stats.tolist()
    print(stats)
    categories=labels.tolist()
    print(categories)
    N = len(categories)
     
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=stats
    values += values[:1]
    print(values) 
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    print(angles) 
    # Initialise the spider plot
    #ax = plt.subplot(111, polar=True)
    fig = plt.figure()
    ax = plt.subplot(111, polar=True)
    
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    for label,a in zip(ax.get_xticklabels(),range(0,len(angles))):
    
        angle_rad=angles[a]
        if angle_rad <= pi/2:
            ha= 'left'
            va= "bottom"
    
        elif pi/2 < angle_rad <= pi:
            ha= 'right'
            va= "bottom"
    
        elif pi < angle_rad <= (3*pi/2):
            ha= 'right'
            va= "top"  
    
        else:
            ha= 'right'
            va= "bottom"
    
        label.set_verticalalignment(va)
        label.set_horizontalalignment(ha)




     
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=7)
    plt.ylim(0,5)
    #i = i.join('\n')
    
    stitle = "\n".join(wrap(i,60))
    stitle = stitle + "\n"
    plt.title(stitle) 
    
    #ax.set_title(i)
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
     
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.savefig(str(answer)+'-radar.png', bbox_inches='tight', dpi=300)
    answer = answer + 1
    
    
