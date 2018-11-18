import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from textwrap import wrap

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)
# assign easier to type values in region column
def area(x):
    if x.startswith('SE'):
        return 'SE'
    elif x.startswith('SW'):
        return 'SW'
    elif x.startswith('NW'):
        return 'NW'
    elif x.startswith('EC'):
        return 'EC'
    elif x.startswith('E'):
        return 'E'
    elif x.startswith('N'):
        return 'N'
    else:
        return 'Outer London'
# respondents who refused an answer are not included in the analysis 
df = df[df['postcode'] != 'I would prefer not to say']
df.postcode.cat.remove_categories('I would prefer not to say', inplace=True)
def transformPostcode(df):
    df['postcode'] = df['postcode'].apply(area)
    return df

df = transformPostcode(df)
# count the frequency for each category
counts = df['postcode'].value_counts(sort=True)

# calcuate percentages from counts
pct = counts / counts.sum() * 100

fig, ax = plt.subplots()
# Function to map the colors as a list from the input list of x variables (value counts)
def pltcolor(lst):
    cols=[]
    for l in lst:
        if l==10:
            cols.append('#004c6d')
        elif l==7:
            cols.append('#247392')
        elif l == 5:
            cols.append('#449cb7')
        elif l == 3:
            cols.append('#66c7dc')
        else:
            cols.append('#8bf3ff')
    return cols
# Create the colors list using the function above
cols=pltcolor(df['postcode'].value_counts())

# make bar chart of postcode data
pct.plot(kind='barh',
ax = ax,
color=cols,
rot=0)
ax.set_xlabel('%')
ax.set_ylabel('Postcode area')
plt.title("Postcode area of respondents", pad=20, weight='heavy')
plt.tight_layout()
plt.show()