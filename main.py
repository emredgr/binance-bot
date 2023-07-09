from api_connection.connectAPI import ConnectBinance
from utils.read_config import ReadConfiguration
from extract.fetch import FetchData
from utils.argparser import ArgumentParser
from transform.generator import DataGenerator
from transform.casting import TypeConverter 
from transform.clean import DataCleaner 

from pandas import DataFrame
from logging import basicConfig, INFO, info

class Manager(object):
    """Class for managing the data fetching process."""
    
    def __init__(self) -> None:
        # Basic functions to be used in the project are started and variables are defined.
        config_reader = ReadConfiguration(config_file_path="./configurations/config.yaml")
        configurations: dict= config_reader.readConfig()

        connection_data = configurations["Connection"]
        self.time_interval = configurations["Time_Interval"][True]
        self.start_date = configurations["Date_Range"]["start_date"]
        self.stop_date = configurations["Date_Range"]["stop_date"]
        

        connection = ConnectBinance(config_binance_data=connection_data)
        self.client = connection.connect()
    
    
    def getScriptArguments(self)-> dict:
        # get and returns the arguments passed to the main.py script.

        argparser = ArgumentParser()
        arguments:dict = argparser.getScriptArguments()
        return arguments
    
    def fetchData(self, coin_name: str)-> DataFrame:
        # fetch and returns data in the given date range from the api for the given coin_name.

        fetcher = FetchData(self.client, coin= coin_name, time_interval= self.time_interval,
                          start_date= self.start_date, stop_date= self.stop_date)

        dataframe: DataFrame= fetcher.fetchData()        
        return dataframe
    
    
    def convertData(self, data: DataFrame)-> DataFrame:
        # manages type casting operations on data and returns edited data

        converter = TypeConverter(dataframe= data)
        data = converter.applyCasting()
        return data
    
    def generateData(self,data: DataFrame)-> DataFrame:
        # manages the process of generating different data by using the information in the data. And it returns data.

        generator = DataGenerator(dataframe=data)
        generated_data: DataFrame= generator.generateData()
        return generated_data
    
    def cleanData(self, data: DataFrame)-> DataFrame:
        # manages the process of cleaning the data and returns the cleaned data.
        cleaner = DataCleaner(dataframe= data)
        cleaned_data: DataFrame= cleaner.cleanData()
        return cleaned_data

    def isDataExtract(self, data: DataFrame, output_path: str):
        # If output path is given, it will output the data in csv format to the given path
        if output_path is not None:
            data.to_csv(output_path, index=False)
            info(f"Data extracted. Check to the {output_path} path")

            


def main():
    manager=Manager()
    script_args: dict= manager.getScriptArguments()
    data: DataFrame= manager.fetchData(coin_name=script_args.get("coin"))
    data: DataFrame = manager.convertData(data= data)
    data: DataFrame= manager.generateData(data=data)
    data: DataFrame = manager.cleanData(data= data)
    manager.isDataExtract(data= data, output_path= script_args.get("output_path"))


if __name__ == "__main__":
    basicConfig(level=INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
    main()
