import pandas as pd
import numpy as np

#Here we read all the data from the csv file from drive, keep the backup of the data and see the informations of the same.
stock_data= pd.read_csv('/content/stock_list.csv', header=0, na_values='?')
stock_data_backup= stock_data.copy()
stock_data.info()
print(stock_data.isna().any(),"\n")
#We can now see that the columns that require cleaning are NewMarketSegment, TradeDate, Close, IssuedShares and MarketCapitalization

print("NewMarketSegment-> Null Values= ",stock_data['NewMarketSegment'].isna().sum())
print("TradeDate-> Null Values= ",stock_data['TradeDate'].isna().sum())
print("Close-> Null Values= ",stock_data['Close'].isna().sum())
print("IssuedShares-> Null Values= ",stock_data['IssuedShares'].isna().sum())
print("MarketCapitalization-> Null Values= ",stock_data['MarketCapitalization'].isna().sum())
# here we can see that NewMarketSegment has 645, TradeDate has 296, Close has 296, IssuedShares has 296 and MarketCapitalization has 296 data values missing.

