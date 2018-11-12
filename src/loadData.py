import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#path = './data/survey_responses.csv'
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
