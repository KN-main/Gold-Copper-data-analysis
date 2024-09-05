import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('clean_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

# Correlation matrix
corr_matrix = df.corr()

plt.figure(figsize=(10, 6))

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')

plt.title('Correlation Matrix')

plt.show()

# Time Series of Economic Indicators
df.plot(subplots=True, layout=(3, 2), figsize=(10, 8), title='Time Series of Economic Indicators')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()