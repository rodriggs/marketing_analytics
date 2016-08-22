import pandas as pd
import numpy as np
import statsmodels.api as sms

class CleanNanigans(object):
    """
    INPUT: Filename of Nanigans csv data file

    """
    def __init__(self, path):
        self.path = path
        self.load_data()

    def load_data(self):
        df_total = pd.read_csv(self.path)

        df_spent = df_total[df_total["Spend"] > 0]

        columns_to_use = ['Audience - Age',
                            'Audience - Gender',
                            'Creative - Video',
                            'Placement - Current Bid Type',
                            'Context',
                            'CPI (Total Spend/Initiate Checkouts)',
                            'Placement - Status Description']

        self.loaded_data = df_spent[columns_to_use]

    def clean_data(self):
        df = self.loaded_data
        df.fillna(0, inplace=True)
        df['Creative - Video'] = df['Creative - Video'].apply(lambda x: 0 if x == '[blank]' else 1)

        columns_to_dummy = ['Audience - Age',
                            'Audience - Gender',
                            'Creative - Video',
                            'Placement - Current Bid Type',
                            'Context',
                            'Placement - Status Description']

        df = pd.get_dummies(df, columns=columns_to_dummy, drop_first=True)
        df = df.reset_index(drop=True)
        self.df = df
        self.column_names = df.columns
