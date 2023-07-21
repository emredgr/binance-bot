
from datetime import datetime
from pandas import DataFrame,to_numeric
from logging import info, warning

class TypeConverter(object):

    def __init__(self,dataframe: DataFrame) -> None:
        self.dataframe = dataframe

    def toUnixTime(self):

        try:
            self.dataframe["timestamp"] = self.dataframe["timestamp"].apply(lambda x: datetime.fromtimestamp(x/1000.0))
        except Exception as ex:
            warning(f"Error while type casting to unix time format, \nerror message : {ex}")

    def toNumeric(self):

        try:
            self.dataframe['close'] = to_numeric(self.dataframe['close'], errors='coerce')

        except Exception as ex:
            warning(f"Error while type casting to numeric format, \nerror message : {ex}")

    