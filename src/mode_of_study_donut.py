import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from make_donut import *


path = './data/survey_responses.csv'

#load and preprocess data
df = loadData(path)
df = convertDataType(df)

fig, ax = plt.subplots(figsize=(6, 4))
# Set aspect ratio to be equal so that pie is drawn as a circle
ax.axis('equal')
width = 0.3

# use the colormap in Matplotlib
cm = plt.get_cmap("tab20c")

# inside ring
cin = cm(np.arange(3)*4)
labels_in = df.mode_of_study.cat.categories
#labels_in = ['FT', 'PT', 'o']
pie, _ = ax.pie(df['mode_of_study'].value_counts(sort=False), radius=1-width,colors=cin)
plt.setp(pie, width=width, edgecolor='white')
plt.legend(pie, labels_in, loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

# outside ring
cout = cm(np.array([1,2,3,6,7,10]))
labels_out = df.level_of_study.cat.categories
wedges, texts = pie2, _ = ax.pie(df['level_of_study'].value_counts(sort=False), radius=1, colors=cout)
plt.setp(pie2, width=width, edgecolor='white')


data = df['level_of_study'].value_counts(sort=False)
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(xycoords='data', textcoords='data',  arrowprops=dict(arrowstyle="-"), bbox=bbox_props, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(labels_out[i], xy=(x, y),xytext=(1.15*np.sign(x), 1.4*y),
             horizontalalignment=horizontalalignment, **kw)
plt.subplots_adjust(left=0.3)
plt.tight_layout()
plt.show()