import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from textwrap import wrap

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# respondents who refused an answer are not included in the analysis 
df = df[df['postcode'] != 'I would prefer not to say']
df.postcode.cat.remove_categories('I would prefer not to say', inplace=True)

# count the frequency for each category
counts = df['postcode'].value_counts(sort=True)

# calcuate percentages from counts
pct = counts / counts.sum() * 100

fig, ax = plt.subplots()
colours=['#004c6d', '#247392', '#449cb7', '#66c7dc', '#8bf3ff']

# Function to map the colors as a list from the input list of x variables (value counts)
def pltcolor(lst):
    cols=[]
    for l in lst:
        if l==7:
            cols.append('#004c6d')
        elif l==5:
            cols.append('#247392')
        elif l == 3:
            cols.append('#449cb7')
        elif l == 2:
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
ax.set_ylabel('Postcode')
plt.title("Term time postcode of respondents", pad=20, weight='heavy')
plt.tight_layout()
plt.show()