from pandas import DataFrame
from logging import info, warning

class DataGenerator(object):

    def __init__(self, dataframe: DataFrame) -> None:
        self.dataframe = dataframe
        self.column_names = []
    def addRSI(self):
        """RSI (Relative Strength Index)
        
        Calculates the RSI value from the 'close' column data.
        First, it calculates the increases and decreases of the data changes.
        Then, it calculates the averages of the gains and losses, and calculates the RSI using these averages.
        """
        try:

            delta = self.dataframe['close'].diff()
            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)
            avg_gain = gain.rolling(window=14).mean()
            avg_loss = loss.rolling(window=14).mean()
            rs = avg_gain / avg_loss
            self.dataframe['RSI'] = 100 - (100 / (1 + rs))
        except Exception as ex:
            warning(f"""Error while adding RSI indicator to self.dataframe,
                             \n Exception message : {ex}""")
        

    def addMACD(self):
        """MACD (Moving Average Convergence Divergence)
        
        Calculates the MACD and MACD signal values from the 'close' column data.
        First, it calculates the 12-period exponential moving average (EMA) and the 26-period EMA.
        Then, it calculates the MACD value as the difference between these two EMAs.
        Finally, it calculates the MACD signal value using a 9-period EMA.
        
        """
        try:
        
            ema_12 = self.dataframe['close'].ewm(span=12, adjust=False).mean()
            ema_26 = self.dataframe['close'].ewm(span=26, adjust=False).mean()
            macd = ema_12 - ema_26
            signal = macd.ewm(span=9, adjust=False).mean()
            self.dataframe['MACD'] = macd
            self.dataframe['MACD_signal'] = signal

        except Exception as ex:
            warning(f"""Error while adding MACD indicator to self.dataframe,
                             \n Exception message : {ex}""")
        
        

    def addSMA(self):
        """ SMA (Simple Moving Average)
        
        Calculates the simple moving average of the last 14 periods of the 'close' column data.
        """
        try:

            self.dataframe['SMA'] = self.dataframe['close'].rolling(window=14).mean()
        except Exception as ex:
            warning(f"""Error while adding SMA indicator to self.dataframe,
                             \n Exception message : {ex}""")
        
    
    def generateData(self)-> DataFrame:
        
        self.addSMA()
        self.addRSI()
        self.addMACD()
        
        info(f"Added SMA, RSI, MACD and MACD_signal columns to the data.")

        return self.dataframe
