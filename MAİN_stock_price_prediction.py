import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load the dataset
df = pd.read_csv('sp500_stocks.csv')

# Select a specific stock (e.g., Apple - AAPL)
stock_df = df[df['Symbol'] == 'MSFT']
stock_df = stock_df[['Date', 'Close']].sort_values('Date')
stock_df['Date'] = pd.to_datetime(stock_df['Date'])
stock_df.set_index('Date', inplace=True)

# Data Preprocessing
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(stock_df)

# Prepare the training data
train_data_len = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_data_len]
x_train, y_train = [], []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build the LSTM model
model = Sequential([
    LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(units=50, return_sequences=False),
    Dropout(0.2),
    Dense(units=25),
    Dense(units=1)
])

model.compile(optimizer=Adam(), loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=64, epochs=10)

# Test Data Preparation
test_data = scaled_data[train_data_len - 60:]
x_test, y_test = [], stock_df['Close'][train_data_len:]

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Predictions
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# Visualize results
plt.figure(figsize=(10, 6))
plt.plot(stock_df['Close'], color='blue', label='Actual Prices')
plt.plot(stock_df.index[train_data_len:], predictions, color='red', label='Predicted Prices')
plt.title('Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()


model.save(f'lstm_stock_price_model_.h5')
print(f"Model saved as 'lstm_stock_price_model_.h5")