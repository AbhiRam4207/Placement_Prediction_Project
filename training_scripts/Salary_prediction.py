import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing

# Load correct dataset (fix path if needed)
df = pd.read_csv('Salary_prediction_data.csv')

# Drop unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Fill NaNs with 0
df.fillna(0, inplace=True)

# Check and adjust column names
print(df.columns)

# Drop ID and target from features
x = df.drop(['StudentId', 'salary'], axis=1)  # remove 'StudentId' if not present
y = df['salary']

# Encode categorical
le = preprocessing.LabelEncoder()
x['Internship'] = le.fit_transform(x['Internship'])
x['Hackathon'] = le.fit_transform(x['Hackathon'])
x['PlacementStatus'] = le.fit_transform(x['PlacementStatus'])

# Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

# Train
classify = RandomForestRegressor(n_estimators=100, criterion="squared_error")
classify.fit(x_train, y_train)

# Save model
with open('model1.pkl', 'wb') as f:
    pickle.dump(classify, f)

print("✅ model1.pkl created successfully")
