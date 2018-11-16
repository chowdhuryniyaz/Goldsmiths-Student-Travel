import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# use visually equidistant colours
colours = ['#ffa600', '#ff6361', '#bc5090', '#58508d', '#003f5c']
fig, ax = plt.subplots(figsize=(6, 4))
# create donut chart from mode_of_transport column
ax.pie(df.mode_of_transport.value_counts(),
        colors=colours,
        labels=df.mode_of_transport.cat.categories,
        startangle=90,
        wedgeprops = {'linewidth': 0.5, 'edgecolor' : 'lightgrey', 'width':0.5},
        textprops={'size': 'small', 'weight':'heavy'},
        autopct='%.0f%%',
        pctdistance=0.75, 
        labeldistance=1.1)

# add title
plt.title("Main mode of transport", weight='heavy', pad=30)

plt.tight_layout()
# to save the chart as a png image, uncomment the line below
#plt.savefig("mode_of_transport_pie.png", bbox_inches="tight")
plt.show()
