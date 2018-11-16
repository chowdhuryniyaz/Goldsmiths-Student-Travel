from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from make_donut import make_donut

path = './data/survey_responses.csv'
# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# term time accommodation
# respondents who refused an answer are not included in the analysis 
df = df[df['accommodation_type'] != 'other']
df.accommodation_type.cat.remove_categories('other', inplace=True)
df = df[['accommodation_type']]

# make donut chart and save result as png
make_donut(df, column='accommodation_type', title='Accommodation type')