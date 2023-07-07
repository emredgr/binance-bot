from api_connection.connectAPI import ConnectBinance
from configurations.read_config import ReadConfiguration
from extract.fetch import FetchData
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
        
    def fetchData(self):
        fetcher = FetchData(self.client)
        dataframe: DataFrame= fetcher.fetchData(coin= "BTC", time_interval= self.time_interval,
                          start_date= self.start_date, stop_date= self.stop_date)
        logging.info(f" Fetched data count : {dataframe.shape}")
        

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
    
    manager=Manager()
    manager.fetchData()
