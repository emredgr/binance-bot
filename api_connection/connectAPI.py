from binance.client import Client
from typing import Union
from logging import info

class ConnectBinance:
    """Class used for connecting to the Binance API."""

    def __init__(self, config_binance_data) -> None:
        """
        Initialize ConnectBinance class.

        Args:
            config_binance_data (dict): Configuration data containing Binance API key and secret.
        """
        self.api_key = config_binance_data['api_key']
        self.api_secret = config_binance_data['api_secret']
    
    def connect(self) -> Union[Client, Exception]:
        """
        Connects to the Binance API and returns the client object.

        Returns:
            Union[None, Client]: Binance API client object, or None if the connection fails.
        """
        try:
            self.client = Client(self.api_key, self.api_secret)
            
            
            self.client.get_account_status() # used to check api connection

        except Exception as ex:
            raise Exception(f"API connection failed, check the API_KEY and API_SECRET_KEY, \n Exception Message -> {ex}")
        
        else:
            info("Binance Api connection successful")
            return self.client
