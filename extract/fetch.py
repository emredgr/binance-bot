from binance.client import Client
from pandas import DataFrame,to_datetime
from datetime import datetime
import logging

class FetchData(object):

    def __init__(self, client: Client) -> None:
        self.client: Client = client
        
    def fetchData(self, coin: str, start_date: str,
                        stop_date: str, time_interval: str) -> DataFrame:
        
        coin: str = f"{coin}USDT"
        start_date: str = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d %H:%M:%S")
        stop_date: str =  datetime.strptime(stop_date, "%Y-%m-%d").strftime("%Y-%m-%d %H:%M:%S")

        logging.info(f"Fetching data for {coin} coin within the date range of {start_date} to {stop_date}.")

        data = self.client.get_historical_klines(symbol= coin, interval= time_interval,
                                                 start_str= start_date, end_str= stop_date)
        
        df: DataFrame = DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        
        return df
                    