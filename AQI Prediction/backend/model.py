import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
data = pd.read_csv('AQI-and-Lat-Long-of-Countries.csv')
print(data.head())
data = data.dropna()
data.columns = [col.strip().lower() for col in data.columns]
sns.pairplot(data)
plt.show()

corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
X = data[['co aqi value', 'ozone aqi value', 'no2 aqi value', 'pm2.5 aqi value']]
y = data['aqi value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Define a filename for your model
model_filename = 'aqi_random_forest_model.joblib'

# Save the trained model
joblib.dump(model, model_filename)

print(f"Model saved successfully to {model_filename}")