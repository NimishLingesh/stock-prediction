# stock-prediction

Dataset: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/data

Pre-processing Collab Notebook: https://colab.research.google.com/drive/13bFdJJmVMlNA3L4ZUi_zbEaFZ21UjedG#scrollTo=0JldAbH11VNn


Code Check in Guidelines:

1. Create a new branch (eg: devansh/implementdashboard) when you start with new Issue/Work Item.
2. Work in that newly created branch
3. Test your changes well.
4. Raise a Pull Request against the main branch. Add rest of the team members as the reviewer.
5. Merge it with the main branch when you have an approval.

Code Progress:
1. The Specifications of each column is now known.
2. Found the columns that have missing data.
3. For this particular data set we see that NewMarketSegment, TradeDate, Close, IssuedShares and MarketCapitalization these 5 columns has missing values.
4. We can see the count of null values as follows:
      NewMarketSegment->  645
      TradeDate-> 296
      Close-> 296
      IssuedShares-> 296
      MarketCapitalization-> 296 
