import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import urllib.request
import json
from textwrap import wrap
from loadData import loadData, convertDataType
import googlemaps
from datetime import datetime
from preprocess_distance_data import preprocess

path = './data/distance_data.csv'
key = 'AIzaSyCPW_wydntgl4BMzn5gqufzJplcCCawdlQ'

# load preprocessed data
df1 = pd.read_csv(path)

df1.loc[((df1['mode_of_transport'] == 'Motor vehicle (car or motorcycle/scooter)') ) , "mode_of_transport"] = 'Motor vehicle'

df2 = pd.crosstab(df1['mode_of_transport'], df1['distance_cat'])

# use visually equidistant colours
cols = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']
ax = df2.plot.barh(stacked=True, figsize=(8,4), color=cols)
handles, labels = ax.get_legend_handles_labels()
labels[0] = 'Less than 1 km'
labels[4] = 'More than 10 km'
labels = [ '\n'.join(wrap(l, 20)) for l in labels ]
ax.legend(handles, labels, bbox_to_anchor=(1.0, 1.0), frameon=False)
#ax.set_xlabel('%')
plt.title('Transport preferences by distance', pad=20)
ax.set_xlabel("Number of students")
ax.set_ylabel("Mode of transport") 
plt.xticks([0,5,10,15,20])

ax.grid(which='both', axis='x',alpha=0.5)
plt.tight_layout()
plt.show()

# save crosstab of main mode and distance categories to csv
#df3 = pd.crosstab(df1['mode_of_transport'], df1['distance_cat'], margins=True)
#df3.to_csv('./data/crosstab_mode_dist.csv')