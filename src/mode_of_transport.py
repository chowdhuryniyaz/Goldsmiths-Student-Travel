import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *
from textwrap import wrap

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# respondents who refused an answer are not included in the analysis 
df.mode_of_transport.cat.remove_categories('other', inplace=True)

# use visually equidistant colours
colours = ['#ffa600', '#ff6361', '#bc5090', '#58508d']

fig, ax = plt.subplots(figsize=(6, 4))

# create pie chart from mode_of_transport column
patches, texts, autotexts = ax.pie(df.mode_of_transport.value_counts(sort=False),
        colors=colours,
        #labels=df.mode_of_transport.cat.categories,
        startangle=60,
        wedgeprops = {'linewidth': 0.5, 'edgecolor' : 'lightgrey', 'width':0.5},
        #textprops={'weight':'heavy'},
        autopct='  %.0f%%',
        pctdistance=0.75, 
        labeldistance=1.1)

for t in autotexts:
        t.set_fontsize(12)
        
# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')
plt.subplots_adjust(bottom=0.1)

# Put a legend next to the chart, hide frame
plt.legend(df.mode_of_transport.cat.categories,bbox_to_anchor=(1,0.5),loc="center left", frameon=False)
plt.title("Usual mode of commuting", pad=30, weight='heavy')
plt.tight_layout()

# to save the chart as a png image, uncomment the line below
#plt.savefig("mode_of_transport_donut.png", bbox_inches="tight", dpi=200)
plt.show()
