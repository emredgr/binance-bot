from binance.client import Client
from pandas import DataFrame
from datetime import datetime
from logging import info

class FetchData(object):

    def __init__(self, client: Client, coin: str, time_interval: str,
                 start_date: str, stop_date: str) -> None:
        
        self.client: Client = client
        
        self.coin = f"{coin}USDT"
        
        self.time_interval = time_interval
        self.start_date =  datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        self.stop_date =  datetime.strptime(stop_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        


    def fetchDataFromBinance(self)-> DataFrame:
        
        data = self.client.get_historical_klines(symbol= self.coin, interval= self.time_interval,
                                                 start_str= self.start_date, end_str= self.stop_date)
        
        dataframe: DataFrame = DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        
        info(f"Data fetched for {self.coin.replace('USDT','')} coin within the date range of {self.start_date} to {self.stop_date}.")
        info(f" Fetched data count : {dataframe.shape[0]}")

        return dataframe
    
    

        
        