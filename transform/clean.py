
from pandas import DataFrame
from logging import info

class DataCleaner(object):

    def __init__(self, dataframe: DataFrame) -> None:
        self.dataframe = dataframe

    def dropNA(self):
        self.dataframe = self.dataframe.dropna()  # drop the NaN values from dataframe

    def cleanData(self)-> DataFrame:
        self.dropNA()
        # add other data cleaning process to here.

        info(f"Data cleaning is complete. The cleaned data is being returned.")
        return self.dataframe