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

fig, ax = plt.subplots()

# plot distribution of avg_journey_time data
# use the cat.codes method to access the underlying numerical values representing the ordered categories
time_codes = df['avg_journey_time'].cat.codes 
time_codes.name = 'Students'
ax = time_codes.plot.box() 
ax.set_ylabel('journey time')
ax.set_yticks([0, 1, 2, 3, 4])
ax.set_yticklabels(labels=df.avg_journey_time.cat.categories)
plt.title("Distribution of average journey time", pad=30, weight='heavy')
plt.tight_layout()
plt.show()
