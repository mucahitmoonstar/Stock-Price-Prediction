**ABOUT DATASET;**

**S&P 500 Stocks (daily updated);**
The Standard and Poor's 500 or S&P 500 is the most famous financial benchmark in the world.
This stock market index tracks the performance of 500 large companies listed on stock exchanges in the United States. As of December 31, 2020, more than $5.4 trillion was invested in assets tied to the performance of this index.
Because the index includes multiple classes of stock of some constituent companies—for example, Alphabet's Class A (GOOGL) and Class C (GOOG)—there are actually 505 stocks in the gauge.
https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks/data

**Apple Stock Market Historical Data (1980-2024);**
This dataset contains daily historical market data for Apple Inc. (AAPL) spanning from December 1980 to March 2024. It includes information such as opening and closing prices, high and low prices, 
trading volume, and percentage change.

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

**Recurrent Neural Network (RNN)**

A Recurrent Neural Network (RNN) is a type of neural network specifically designed to handle sequence data, such as time series, language, and audio. Unlike traditional neural networks, which process inputs independently, RNNs are designed to retain information from previous inputs in the sequence by using loops within the network. This means that an RNN can maintain a "memory" of prior data, allowing it to recognize patterns across sequences, which is especially valuable in tasks where the order of data points is critical.
However, RNNs can struggle with long-term dependencies due to a problem called the vanishing gradient problem, which means that information from earlier time steps can get "lost" as it progresses through the network. This is where LSTM networks come in.

**Long Short-Term Memory (LSTM)**

LSTM, or Long Short-Term Memory, is a type of RNN designed to better capture long-term dependencies in sequence data. LSTMs address the vanishing gradient problem by using a unique architecture that includes gates—the input gate, forget gate, and output gate. These gates control the flow of information, allowing the network to keep or discard information as needed.

**Here's a breakdown of how each gate works:**
Input Gate: Decides how much of the current input should be added to the memory.
Forget Gate: Determines how much of the previous memory should be retained.
Output Gate: Controls the final output and what information should be transferred to the next time step.
This structure enables LSTMs to retain long-term dependencies in a way that traditional RNNs struggle with, making LSTMs especially effective for tasks like language translation, speech recognition, and stock price prediction.

**Structure of the LSTM Algorithm**
LSTM excels at detecting patterns within time-dependent data because it effectively manages both short- and long-term memory, selectively retaining or discarding information as needed. Each LSTM cell can remember previous time steps, analyzing data for potential patterns over time.


**Why We Used LSTM ?**
LSTMs are particularly effective for time series data, like stock prices, which rely on historical data for future predictions. Traditional RNNs struggle with learning long-term dependencies, whereas LSTM retains these dependencies, making it well-suited for analyzing historical trends to forecast future prices. This makes LSTM a powerful choice for predicting Microsoft’s stock prices based on its historical data.




**RESULT;**
In this code, we build a predictive LSTM model for stock prices:

1. **Data Loading and Selection**: We load the stock data (for a specific stock, e.g., Microsoft "MSFT") and filter it to use only the closing prices, indexed by date. This lets us focus on key data for time-series forecasting.

2. **Data Preprocessing**: The data is scaled to a range of 0 to 1 using MinMaxScaler, which helps the LSTM model train more efficiently. We then split the data into a training set (80%) and a testing set (20%) and create sequences of 60 days as inputs, with the target being the next day’s price.

3. **Model Building**: A Sequential model with two LSTM layers is created, with dropout layers to prevent overfitting. The model aims to capture temporal dependencies in stock price movements.

4. **Training**: The model is trained on the processed training data to minimize mean squared error, learning patterns in the historical prices.

5. **Testing and Visualization**: The model is then tested on the testing set, and predictions are made. These predictions are then scaled back to their original values and plotted alongside the actual prices for comparison.

6. **Saving**: Finally, the model is saved as an H5 file for future use.

This approach helps us understand and predict stock price trends based on historical data patterns, making it useful for time-series forecasting tasks like stock price prediction.

We aimed to predict stock prices for Apple, Nvidia, and Microsoft using historical data, each within specific timeframes. For Microsoft, the model was tested on data spanning from 1988 to 2012, for Nvidia from 2000 to 2010, and for Apple from 1980 to 2012. The model successfully predicted the prices within each of these ranges using data from 2010 to 2024 as the training set. This allowed us to leverage modern data to gain insights into past price movements for each company within their unique historical context.


**TRAİN RESULT**

![APPLE train](https://github.com/user-attachments/assets/d3d5b9d4-b932-45a7-adf4-c4ec3dcd5380)


![microsoft train](https://github.com/user-attachments/assets/32c0b3c7-2120-4941-a4c2-4b7e791ce6a8)


![NWDIA TRAİN](https://github.com/user-attachments/assets/62732a3c-067d-4d51-a8ce-02459965f9df)


**TEST RESULT**



![Apple's](https://github.com/user-attachments/assets/2945cb92-1bab-48f4-9235-057ef23f0656)


![microsoft](https://github.com/user-attachments/assets/c17e5132-d18e-4e83-b059-26efbf6d095a)


![NVDIA](https://github.com/user-attachments/assets/00a563d3-7685-4de1-8c46-52f960fe5a67)




