
from pandas import DataFrame
from logging import info

class DataCleaner(object):

    def __init__(self, dataframe: DataFrame) -> None:
        self.dataframe = dataframe

    def dropNA(self):
        self.dataframe = self.dataframe.dropna()  # drop the NaN values from dataframe

   