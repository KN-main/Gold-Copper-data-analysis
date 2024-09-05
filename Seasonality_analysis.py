import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


df = pd.read_csv('clean_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

decomposition = seasonal_decompose(df['Six Month Demand'], model='additive', period=12)

decomposition.plot()
plt.suptitle('Seasonal Decomposition of Six Month Demand', fontsize=16)
plt.show()