Binance Bot
===

This project is a Python application that pulls price data for the specified cryptocurrency using the Binance API and adds technical analysis indicators to the pulled data. The project also includes data cleaning and transformation steps. These steps provide significant benefits to the user to increase the accuracy of the captured data and make it suitable for analysis.

## Configurations
- First, the api_key and api_secret key in the config.yaml file must be set.
- The date range must be specified.
- Time interval value can be determined

## Project Steps
- Data Extraction: The project pulls price data according to the specified start date, end date and time range for the specified cryptocurrency (coin) using the Binance API. This function allows users to perform various analyzes for different coins.

- Data Cleaning: The captured data is checked for availability and accuracy. Data cleanup steps include fixing missing or corrupt data and fixing data incompatibilities. Thus, a more reliable dataset is obtained for analysis.

- Type Casting: Data is converted to appropriate data types. For example, date/time data is converted to an appropriate format or numeric values are converted to appropriate data types. This step ensures that the correct calculations are made for the analysis.

- Validation: The data is checked against the established validation rules. This step helps detect abnormal or incorrect data and improves data reliability.

- Calculation of Technical Indicators: The project calculates technical analysis indicators such as RSI, MACD, MACD signal and SMA based on the captured price data. These indicators provide the user with important information to understand the market trends and momentum.

- Saving to CSV File: The project saves the processed data and calculated technical indicators in a regular CSV file. This file allows users to export data and perform further analysis.

## Install & Dependence
- binance==0.3
- pandas==2.0.3
- python-binance==1.0.17
- PyYAML==6.0

-or the dependencies can be installed directly from the requirements.txt file. use this command:
- pip install -r requirements.txt


## Use
- for bitcoin
  ```
  python main.py -c BTC -o output.csv
  ```



## Directory Hierarchy
```
|—— api_connection
|    |—— connectAPI.py
|—— configurations
|    |—— config.yaml
|—— extract
|    |—— fetch.py
|—— transform
|    |—— casting.py
|    |—— clean.py
|    |—— generator.py
|    |—— __init__.py
|—— utils
|    |—— argparser.py
|    |—— read_config.py
|—— main.py
|—— requirements.txt
|—— test


```
