
from pandas import DataFrame


class DataCleaner:

    def __init__(self, dataframe: DataFrame) -> None:
        self.dataframe = dataframe

    def dropNA(self):
        self.dataframe = self.dataframe.dropna()  # drop the NaN values from dataframe

   