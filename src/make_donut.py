import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype

def make_donut(df, column, title):
    # use visually equidistant colours
    colours = ['#ffa600', '#ff6361', '#bc5090', '#58508d']

    fig, ax = plt.subplots(figsize=(6, 4))

    column = df[column]
    # create pie chart from specified column
    patches, texts, autotexts = ax.pie(column.value_counts(sort=False),
            colors=colours,
            #labels=df.column.cat.categories,
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
    plt.legend(column.cat.categories,bbox_to_anchor=(1,0.5),loc="center left", frameon=False)
    plt.title(title, pad=30, weight='heavy')
    plt.tight_layout()

    # save the chart as a png image
    plt.savefig('{}.png'.format(title), bbox_inches="tight", dpi=200)
    
    plt.show()
