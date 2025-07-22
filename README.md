# Tariff Sensitivity
This code calculates the sensitivity (beta) of stocks in the S&P 500 to the return of the S&P 500 on days when important tariff announcements were made.

The days with important tariff announcements are inferred from [this New York Times article](https://www.nytimes.com/2025/03/13/business/economy/trump-tariff-timeline.html). If the news is on a non-trading day, the next trading day is assumed to be impacted by the news.

The daily returns of each stock (all constituents of the S&P 500) are then regressed on the returns of the S&P 500 and a vector that contains the returns of the S&P 500 when there are important tariff announcements, and 0 otherwise. The coefficient (beta) to this vector informs about the sensitivity of a stock to the tariff news:

$$
r_i = \alpha + \beta_1 \cdot r_{\text{SP 500}} + \beta_2 \cdot r_{\text{SP 500 when news}} + \varepsilon_i
$$

After running the code, these stocks show up as being most sensitive to tariffs:

| Company Name                              | Beta to Market | Beta to Tariffs |
|-------------------------------------------|----------------|-----------------|
| APA Corporation                           | 0.83           | 1.32            |
| Halliburton Company                       | 0.38           | 1.25            |
| Skyworks Solutions, Inc.                  | 0.93           | 1.08            |
| Devon Energy Corporation                  | 0.62           | 1.06            |
| Microchip Technology Incorporated         | 1.57           | 1.04            |
| United Airlines Holdings, Inc.            | 1.39           | 0.94            |
| Dow, Inc.                                 | 0.72           | 0.94            |
| Diamondback Energy, Inc.                  | 0.60           | 0.94            |
| Schlumberger Limited                      | 0.51           | 0.88            |
| Delta Air Lines, Inc.                     | 1.19           | 0.86            |

And these stocks show up as being least sensitive to tariffs:

| Company Name                                 | Beta to Market | Beta to Tariffs |
|----------------------------------------------|----------------|-----------------|
| Molina Healthcare, Inc.                      | 0.75           | -0.85           |
| Humana Inc.                                  | 0.96           | -0.84           |
| PulteGroup, Inc.                             | 1.32           | -0.74           |
| Coinbase Global, Inc. Class A                | 2.59           | -0.74           |
| Palantir Technologies Inc. Class A           | 2.65           | -0.74           |
| Super Micro Computer, Inc.                   | 2.63           | -0.74           |
| Centene Corporation                          | 0.58           | -0.68           |
| First Solar, Inc.                            | 1.50           | -0.63           |
| Erie Indemnity Company Class A               | 0.90           | -0.62           |
| Fair Isaac Corporation                       | 1.49           | -0.61           |


