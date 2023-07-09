from binance.client import Client
from pandas import DataFrame
from datetime import datetime
from logging import info

class FetchData(object):

    def __init__(self, client: Client, coin: str, time_interval: str,
                 start_date: str, stop_date: str) -> None:
        self.dataframe = DataFrame()

        self.client: Client = client
        self.coin = coin
        self.time_interval = time_interval
        self.start_date = start_date
        self.stop_date = stop_date
        
    def fetchDataFromBinance(self):
        
        coin: str = f"{self.coin}USDT"
        start_date: str = datetime.strptime(self.start_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        stop_date: str =  datetime.strptime(self.stop_date, "%Y-%m-%d").strftime("%Y-%m-%d")


        

        data = self.client.get_historical_klines(symbol= coin, interval= self.time_interval,
                                                 start_str= start_date, end_str= stop_date)
        
        self.dataframe: DataFrame = DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        
        info(f"Data fetched for {self.coin} coin within the date range of {start_date} to {stop_date}.")
        info(f" Fetched data count : {self.dataframe.shape[0]}")


    def fetchData(self):
        self.fetchDataFromBinance()
    
        return self.dataframe
    

        
        