import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *

path = './data/survey_responses.csv'

df = loadData(path)
df = convertDataType(df)

df = df[df['mode_of_transport'] == 'walking']
df = df[['feel_safe_walking', 'gender']]

df = df[df['gender'] == 'Female']
counts = df['feel_safe_walking'].value_counts(sort = False)
percentage = counts/counts.sum() * 100

fig, ax = plt.subplots()
colours = ['#004c6d', '#247392', '#449cb7', '#66c7dc', '#8bf3ff']

percentage.plot(kind = 'barh',
                ax =ax,
                color = colours,
                rot = 0)

ax.set_xlabel('Percentage %')
ax.set_ylabel('Level of safety')
plt.title("How safe do females feel walking to Goldsmiths", pad=20, weight='heavy')
plt.tight_layout()
plt.show()