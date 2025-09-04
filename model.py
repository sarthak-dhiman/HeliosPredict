import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score, mean_absolute_percentage_error, mean_squared_error

file_path = r'D:\GithubProject\HeliosPredict\RTP_Data\solar_production.xlsx'
df = pd.read_excel(file_path)


features = ['uv_index', 'condition', 'cloud_cover', 'temp_c', 'humidity', 'wind_kph']
target = 'power_kw'

X = df[features]
y = df[target]


num_features = ['uv_index', 'cloud_cover', 'temp_c', 'humidity', 'wind_kph']
cat_features = ['condition']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
])

X_processed = preprocessor.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)


model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)  
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])


history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=16)


y_pred = model.predict(X_test)
test_loss, test_mae = model.evaluate(X_test, y_test)

r2 = r2_score(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100
rmse = mean_squared_error(y_test, y_pred, squared=False)

print(f"Test MAE: {test_mae:.4f}")
print(f"R² Score: {r2:.4f}")
print(f"MAPE: {mape:.2f}%")
print(f"RMSE: {rmse:.4f}")

future_weather = pd.DataFrame([
    {'uv_index': 7, 'condition': 'Sunny', 'cloud_cover': 0, 'temp_c': 30, 'humidity': 40, 'wind_kph': 10}
])
future_weather_processed = preprocessor.transform(future_weather)
predicted_power = model.predict(future_weather_processed)

print(f"Predicted Power Generation: {predicted_power[0][0]:.2f} kW")
