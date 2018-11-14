import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *
import matplotlib.patheffects as path_effects

path = './data/survey_responses.csv'

df = loadData(path)
df = convertDataType(df)
colours = ['#ffa600', '#ff6361', '#bc5090', '#58508d', '#003f5c']

# create pie chart from mode_of_transport column
plt.pie(df.mode_of_transport.value_counts(),
        colors=colours,
        labels=df.mode_of_transport.cat.categories,
        startangle=90,
        wedgeprops = {'linewidth': 0.5, 'edgecolor' : 'lightgrey'},
        textprops={'size': 'small', 'weight':'heavy'},
        autopct='%.0f%%')

# create legend
#plt.legend(df.mode_of_transport.cat.categories,loc="upper left",bbox_to_anchor=(0.85, 0, 0.5, 1))

# add title
plt.title("Main mode of transport")
plt.tight_layout()
plt.show()
# to save the chart as a ong image, uncomment the line below
#plt.savefig("mode_of_transport_pie.png", bbox_inches="tight")