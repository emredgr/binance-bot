from api_connection.connectAPI import ConnectBinance
from utils.read_config import ReadConfiguration
from extract.fetch import FetchData
from utils.argparser import ArgumentParser
from transform.generator import DataGenerator
from transform.casting import TypeConverter 
from transform.clean import DataCleaner 

from pandas import DataFrame
import logging

class Manager(object):
    """Class for managing the data fetching process."""
    def __init__(self) -> None:
        
        config_reader = ReadConfiguration(config_file_path="./configurations/config.yaml")
        configurations: dict= config_reader.readConfig()

        connection_data = configurations["Connection"]
        self.time_interval = configurations["Time_Interval"][True]
        self.start_date = configurations["Date_Range"]["start_date"]
        self.stop_date = configurations["Date_Range"]["stop_date"]
        

        connection = ConnectBinance(config_binance_data=connection_data)
        self.client = connection.connect()
    
    
    def getScriptArguments(self)-> dict:
        argparser = ArgumentParser()
        arguments:dict = argparser.getScriptArguments()
        return arguments
    
    def fetchData(self, coin_name: str)-> DataFrame:
        fetcher = FetchData(self.client, coin= coin_name, time_interval= self.time_interval,
                          start_date= self.start_date, stop_date= self.stop_date)

        dataframe: DataFrame= fetcher.fetchData()        
        return dataframe
    
    
    def convertData(self, data: DataFrame)-> DataFrame:
        converter = TypeConverter(dataframe= data)
        data = converter.applyCasting()
        logging.info("Data type conversions completed successfully")
        return data
    
    def generateData(self,data: DataFrame)-> DataFrame:
        generator = DataGenerator(dataframe=data)
        generated_data: DataFrame= generator.generateData()
        return generated_data
    
    def cleanData(self, data: DataFrame)-> DataFrame:
        cleaner = DataCleaner(dataframe= data)
        cleaned_data: DataFrame= cleaner.cleanData()
        return cleaned_data


def main():
    manager=Manager()
    script_args: dict= manager.getScriptArguments()
    data: DataFrame= manager.fetchData(coin_name=script_args.get("coin"))
    data: DataFrame = manager.convertData(data= data)
    data: DataFrame= manager.generateData(data=data)
    data: DataFrame = manager.cleanData(data= data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
    main()
