import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
pd.options.display.float_format = "{:,.2f}".format

def main():

    # Load data
    news = pd.read_csv('tariff_news.csv')
    returns = pd.read_csv('returns.csv', index_col='Date')

    # Add series that contains the S&P 500 return if there is tariff news, and 0 otherwise
    returns['S&P 500 when news'] = returns['S&P 500'] * returns.index.isin(news['Impacted trading day'].unique())

    # Initialize result
    companies = returns.columns[~returns.columns.isin(['S&P 500', 'S&P 500 when news'])]
    result = pd.DataFrame(np.nan, index = companies, columns = ['Beta to market', 'Beta to tariffs'])

    # Perform regressions
    for company in companies:
        model = LinearRegression().fit(returns[['S&P 500', 'S&P 500 when news']], returns[company])
        result.loc[company, 'Beta to market'] = model.coef_[0]
        result.loc[company, 'Beta to tariffs'] = model.coef_[1]

    # Print top 10 companies with highest beta to tariffs
    print(result.nlargest(10, 'Beta to tariffs'))

    # Print bottom 10 companies with lowest beta to tariffs
    print(result.nsmallest(10, 'Beta to tariffs'))

if __name__ == '__main__':
    main()
