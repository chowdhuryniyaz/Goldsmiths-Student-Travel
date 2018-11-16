from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from make_donut import make_donut

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# respondents who refused an answer are not included in the analysis 
df.mode_of_transport.cat.remove_categories('other', inplace=True)

# make donut chart and save result as png
make_donut(df, column='mode_of_transport', title='Usual mode of commuting')