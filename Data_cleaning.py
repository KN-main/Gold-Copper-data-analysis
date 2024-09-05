import pandas as pd


df = pd.read_csv('df.csv')

df.rename(columns={'DATE': 'Date', 'COPPER_PRICE': 'Copper Price', 'BUY_PRICE' : 'Buy Price',
    'GLOBAL_CONSUMER_PRICE_INDEX': 'Global Consumer Price Index', 'SIX_MONTH_DEMAND': 'Six Month Demand', 
    'GOLD_PRICE': 'Gold Price', 'INVENTORY': 'Inventory'}, inplace=True)

df = df.drop_duplicates()

df = df.dropna()

df.to_csv('clean_data.csv', index=False)

print(df.head())

print(df.columns)