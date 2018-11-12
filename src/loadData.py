import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype


path = './data/survey_responses.csv'
def loadData(path):
    """
    Load the data into a Pandas DataFrame. 
    Skip the first row (header) and rename the columns 
    Args:
        path: String path to dataset.
    Returns:
        df: Data as a Pandas DataFrame.
    """
    colnames = ['timestamp', 'postcode', 'accomodation_type', 'avg_journey_time', 
    'arr_monday', 'arr_tuesday', 'arr_wednesday', 'arr_thursday', 'arr_friday', 
    'dep_monday', 'dep_tuesday', 'dep_wednesday', 'dep_thursday', 'dep_friday', 'mode_of_transport',
    'why_public_transport', 'modes_pt', 'station', 'ticket_type',
    'why_motor_vehicle', 'driver_or_passenger', 'park_vehicle', 'consider_changes', 
    'why_walk', 'route', 'pedestrian_crossings', 'congested_route', 'walk_alone', 'well_maintained_pavements', 
    'litter_on_route', 'lighting_at_night', 'pavements_not_wide', 'feel_safe_walking', 
    'why_cycle', 'park_bike', 'bike_safety', 'feel_safe_cycling',
    'why_other', 
    'age', 'gender', 'level_of_study', 'year_of_study', 'region']
    
    df = pd.read_csv(path, names=colnames, header=None, skiprows=1, index_col=False)

    return df

def convertDataType(df):
    """
    Convert data types to categorical
    Args:
        df: Data as Pandas DataFrame
    Returns:
        df: Data as a Pandas DataFrame, with categorical columns
    """
    # set data type of postcode column as nominal
    postcode_type = CategoricalDtype(ordered=False, categories=['SE14', 'E14', 'NW4', 'SE8', 'N8', 'E4', 'NW1', 
    'other', 'E3', 'SE1', 'SW2', 'E10', 'N15', 'E2', 'SE18', 'N1', 'EC2', 'SE4'])
    df['postcode'] = df['postcode'].map({'SE14 New Cross': 'SE14', 'Other': 'other', 'E14 Poplar': 'E14',
    'I would prefer not to say': 'other', 'NW4 Hendon': 'NW4', 'SE8 Deptford': 'SE8', 'N8 Hornsey': 'N8',
    'E4 Chingford': 'E4', 'NW1 Head district': 'NW1', 'E3 Bow': 'E3', 'SE1 Head district': 'SE1', 
    'SW2 Brixton': 'SW2', 'E10 Leyton': 'E10', 'N15 South Tottenham': 'N15', 'E2 Bethnal Green': 'E2',
    'SE18 Woolwich': 'SE18', 'N1 Head district': 'N1', 'EC2 Bishopsgate': 'EC2', 'SE4 Brockley': 'SE4'}).astype(postcode_type)

    # set data type of accomodation_type column as nominal
    accomodation_types = CategoricalDtype(ordered=False, categories=['rent', 'own_home', 'halls_of_residence', 'with_parents', 'other'])
    df['accomodation_type'] = df['accomodation_type'].map({'Living with parents/guardians during term time': 'with_parents', 
    'Shared rental accomodation': 'rent', 
    'Your own permanent residence (either owned or rented)': 'own_home',
    'Goldsmiths halls of residence': 'halls_of_residence',
    'I would prefer not to say': 'other', np.NaN: 'other'}).astype(accomodation_types)

    # # set data type of avg_journey_time column as ordinal
    journey_time_type = CategoricalDtype(ordered=True, categories=['Less than 15 minutes', '15 - 30 minutes', '31 - 45 minutes',
    '46 - 60 minutes', 'More than 60 minutes'])
    df['avg_journey_time'] = df['avg_journey_time'].astype(journey_time_type)

    arrival_time_type = CategoricalDtype(ordered=True, categories=['Before 08:00', '08:00 - 10:00', '10:01 - 12:00', 
    '12:01 - 14:00', '14:01 - 16:00', 'After 16:01', 'Did not come to Goldsmiths this day'])
    #df['arr_monday'] = df['arr_monday'].astype(arrival_time_type)
    for col in ['arr_monday', 'arr_tuesday', 'arr_wednesday', 'arr_thursday', 'arr_friday']:
        df[col] = df[col].astype(arrival_time_type)
    
    departure_time_type = CategoricalDtype(ordered=True, categories=['Before 12:00', '12:00 - 14:00', '14:01 - 16:00',
    '16:01 - 18:00', '18:01 - 20:00', 'After 20:01', 'Did not come to Goldsmiths this day'])

    for col in ['dep_monday', 'dep_tuesday', 'dep_wednesday', 'dep_thursday', 'dep_friday']:
        df[col] = df[col].astype(departure_time_type)

    return df

def getDemographics(df):
    """
    Get demographics section only
    Args:
        df: Pandas DataFrame
    Returns:
        demographics_df: Demographic data as a Pandas DataFrame.
    """
    demographics_df = df.loc[:, ['age', 'gender', 'level_of_study', 'year_of_study', 'region']]
    return demographics_df

def getSection1(df):
    """
    Get the first section only, containing general questions
    Args:
        df: Pandas DataFrame
    Returns:
        section1_df: Demographic data as a Pandas DataFrame.
    """
    section1_df = df.loc[:, ['postcode', 'accomodation_type', 'avg_journey_time', 
    'arr_monday', 'arr_tuesday', 'arr_wednesday', 'arr_thursday', 'arr_friday', 
    'dep_monday', 'dep_tuesday', 'dep_wednesday', 'dep_thursday', 'dep_friday', 'mode_of_transport']]
    
    return section1_df

