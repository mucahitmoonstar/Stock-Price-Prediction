**ABOUT DATASET;**

**S&P 500 Stocks (daily updated);**
The Standard and Poor's 500 or S&P 500 is the most famous financial benchmark in the world.
This stock market index tracks the performance of 500 large companies listed on stock exchanges in the United States. As of December 31, 2020, more than $5.4 trillion was invested in assets tied to the performance of this index.
Because the index includes multiple classes of stock of some constituent companies—for example, Alphabet's Class A (GOOGL) and Class C (GOOG)—there are actually 505 stocks in the gauge.
https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks/data

**Apple Stock Market Historical Data (1980-2024);**
This dataset contains daily historical market data for Apple Inc. (AAPL) spanning from December 1980 to March 2024. It includes information such as opening and closing prices, high and low prices, trading volume, and percentage change.
https://www.kaggle.com/datasets/shiivvvaam/apple-stock-market-historical-data-1980-2024

**Microsoft Stock Dataset;**
Microsoft Corporation is an American multinational technology company which produces computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 21 in the 2020 Fortune 500 rankings of the largest United States corporations by total revenue; it was the world's largest software maker by revenue as of 2016. It is considered one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Amazon, and Facebook.
https://www.kaggle.com/datasets/varpit94/microsoft-stock-data


**NVIDIA Corp Share price 2000-2024;**
Nvidia Corporation is a multinational technology company headquartered in Santa Clara, California, United States. It was incorporated in Delaware,United States in 1993. Nvidia Corporation went public on January 22, 1999, and its shares began trading on NASDAQ Stock Market under the ticker symbol of NVDA. NVDA shares are also included as a component on several stock market indices, namely S&P 500, S&P 100 and NASDAQ-100. On November 6, 2020, NVDA stocks reached an all-time highest stock closing price of $582.48.
In 2002, Fortune magazine recognised Nvidia Corporation as the fastest-growing company in the US. NVDA entered in another acquisition in 2003 and bought-off MediaQ Inc. in a transaction of $70 million. Stanford Graduate School of Business Alumni Association named Nvidia Corporation as the Entrepreneurial Company of the Year in 2003. Nvidia GPUs powered all Academy Award Nominees in the category of Best Visual Effects 2010, which included Star Trek and Avatar.
In 2010, it also powered the world's fastest supercomputer at the time - China's Tianhe- 1A. The company made an acquisition in 2020 and purchased Mellanox Technologies, Ltd., a leading producer of networking products at the time, for a purchase price of $7 billion. As of 2021, the company has over 50 offices worldwide, including countries like Sweden, Denmark, Israel, Czech Republic, Poland, Russia, United Arab Emirates, Germany, France, Ukraine, Finland, Switzerland, and the United Kingdom, among others.
NVDA ranked 292nd on the list of Fortune 500 companies. It ranked 489th on Forbes' list of Global 2000 2020 companies. Forbes also included Nvidia Corporation in its 2020 rankings of World's Best Employers, America's Best Employers By State, and Best Employers for Diversity.

**GOAL;**
The goal of this project is to develop a predictive model that, using today’s stock price data, estimates historical stock prices. This reverse prediction approach aims to uncover patterns and trends from the past, providing a unique perspective on how current market conditions might have influenced historical behavior. By analyzing historical price trends through the lens of today’s data, this model can shed light on how different economic factors may have impacted past stock performance, enhancing our understanding of both current and historical market dynamics.


**ALGORİTHM;**

In this project, we used the Long Short-Term Memory (LSTM) algorithm to predict Microsoft's,NVDIA,APPLE'S stock prices. LSTM is a type of Recurrent Neural Network (RNN) specifically designed to model long-term dependencies in time series data.


**Structure of the LSTM Algorithm**
LSTM excels at detecting patterns within time-dependent data because it effectively manages both short- and long-term memory, selectively retaining or discarding information as needed. Each LSTM cell can remember previous time steps, analyzing data for potential patterns over time.


**Why We Used LSTM ?**
LSTMs are particularly effective for time series data, like stock prices, which rely on historical data for future predictions. Traditional RNNs struggle with learning long-term dependencies, whereas LSTM retains these dependencies, making it well-suited for analyzing historical trends to forecast future prices. This makes LSTM a powerful choice for predicting Microsoft’s stock prices based on its historical data.


**RESULT;**
![Apple's](https://github.com/user-attachments/assets/2945cb92-1bab-48f4-9235-057ef23f0656)

![microsoft](https://github.com/user-attachments/assets/c17e5132-d18e-4e83-b059-26efbf6d095a)

![NVDIA](https://github.com/user-attachments/assets/00a563d3-7685-4de1-8c46-52f960fe5a67)

