import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *
from textwrap import wrap

path = './data/survey_responses.csv'

# calculate % from value counts
def pct(df):
    pct = df.apply(lambda x: x.value_counts() / len(x)*100).transpose()
    return pct

#returns x and y position for a given point on a given ax
def get_x_and_y(point, ax):
    x = ax.patches[point].get_width()
    y = ax.patches[point].get_height()
    return x, y

# returns ax size
def get_ax_size(ax):
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi
    return width, height

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# Divide the figure into a 3.3 grid, and give each ax a row
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

# region
# respondents who refused an answer are not included in the analysis 
df_region = df.copy()
df_region = df_region[df_region['region'] != 'other']
df_region.region.cat.remove_categories('other', inplace=True)
df_region = df_region[['region']]


region_pct = pct(df_region)
# plot values as stacked bar
region_pct.plot(ax = ax1,kind='barh', stacked=True, rot=0, width=0.1, color=['#3C8C1A','#70AD56', '#90CC76'], legend=None)

ax1_height, ax1_width = get_ax_size(ax1)
print(ax1_width)
# get width of each bar section
#x1 = ax1.patches[0].get_width()
x1_x, x1_y = get_x_and_y(0, ax1)
print(x1_x)
x2_x, x2_y = get_x_and_y(1, ax1)
x3_x, x2_y = get_x_and_y(2, ax1)
w1=x1_x+x2_x
w2=x1_x+x2_x+x3_x
# add text
ax1.text(0, 0.1, 'Where students come from', fontdict={'fontweight':'bold', 'fontsize':14})
ax1.text(0, -0.15, 'UK: {:.0f}%'.format(x1_x), fontdict={'color':'#3C8C1A', 'fontweight':'heavy', 'fontsize':12})
ax1.text(w2, -0.15, 'EU: {:.0f}%'.format(x2_x), fontdict={'color':'#70AD56', 'fontweight':'heavy', 'fontsize':12, 'horizontalalignment':'right'})
ax1.text(w2, -0.25, 'overseas: {:.0f}%'.format(x3_x), fontdict={'color':'#90CC76', 'fontweight':'heavy', 'fontsize':12, 'horizontalalignment':'right'})
# hide axis
ax1.axis('off')



# level of study
# respondents who refused an answer are not included in the analysis 
df_level = df.copy()
df_level = df_level[df_level['level'] != 'other']
df_level.level.cat.remove_categories('other', inplace=True)
df_level = df_level[['level']]

level_pct = pct(df_level)
# plot values as stacked bar
level_pct.plot(ax = ax2,kind='barh', stacked=True, rot=0, width=0.1, color=['#3C8C1A','#70AD56', '#90CC76'], legend=None)

ax2_height, ax2_width = get_ax_size(ax2)

# get width of each bar section

x4_x, x4_y = get_x_and_y(0, ax2)
x5_x, x2_y = get_x_and_y(1, ax2)
x6_x, x6_y = get_x_and_y(2, ax2)

# add text
ax2.text(0, 0.1, 'Level of study', fontdict={'fontweight':'bold', 'fontsize':14})
ax2.text(0, -0.15, 'Undergraduate: {:.0f}%'.format(x4_x), fontdict={'color':'#3C8C1A', 'fontweight':'heavy', 'fontsize':12})
ax2.text(w2, -0.15, 'Postgraduate: {:.0f}%'.format(x5_x), fontdict={'color':'#70AD56', 'fontweight':'heavy', 'fontsize':12, 'horizontalalignment':'right'})
ax2.text(w2, -0.25, 'Foundation: {:.0f}%'.format(x6_x), fontdict={'color':'#90CC76', 'fontweight':'heavy', 'fontsize':12, 'horizontalalignment':'right'})
# hide axis
ax2.axis('off')



# mode of study
# respondents who refused an answer are not included in the analysis 
df_mode = df.copy()
df_mode = df_mode[df_mode['mode_of_study'] != 'other']
df_mode.mode_of_study.cat.remove_categories('other', inplace=True)
df_mode = df_mode[['mode_of_study']]

mode_pct = pct(df_mode)
# plot values as stacked bar
mode_pct.plot(ax = ax3,kind='barh', stacked=True, rot=0, width=0.1, color=['#3C8C1A','#70AD56'], legend=None)


# get width of each bar section
x7_x, x7_y = get_x_and_y(0, ax3)
x8_x, x8_y = get_x_and_y(1, ax3)


# add text
ax3.text(0, 0.1, 'Mode of study', fontdict={'fontweight':'bold', 'fontsize':14})
ax3.text(0, -0.15, 'Full time: {:.0f}%'.format(x7_x), fontdict={'color':'#3C8C1A', 'fontweight':'heavy', 'fontsize':12})
ax3.text(w2, -0.15, 'Part time: {:.0f}%'.format(x8_x), fontdict={'color':'#70AD56', 'fontweight':'heavy', 'fontsize':12, 'horizontalalignment':'right'})
# hide axis
ax3.axis('off')

plt.tight_layout()
# to save the chart as a png image, uncomment the line below
#plt.savefig("region_barh.png", bbox_inches="tight", dpi=200)
plt.show()
