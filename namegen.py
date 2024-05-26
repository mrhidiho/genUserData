import pandas as pd
import numpy as np

# Read the csv file with user names
df_users = pd.read_csv('users.csv')

# Get the number of rows in df_users
num_users = len(df_users)

# Calculate the number of times each name needs to be repeated
repeats = 100 // num_users

# If there's a remainder, add 1 to repeats
if 100 % num_users != 0:
    repeats += 1

# Define column names
columns = ['NAME', 'groupId', 'att0', 'att1f', 'att2f', 'att3f', 'att4f', 'att5f', 'att6f', 'att7f', 'att8f', 'att9f', 'att1v', 'att2v', 'att3v', 'att4v', 'att5v', 'att6v', 'att7v', 'att8v', 'att9v']

# Create a dictionary to store the data
data = {}

# Populate the 'name' column
data['NAME'] = np.tile(df_users.iloc[:, 0].values, repeats)[:100] # Repeat and slice to 1000

# Populate the 'groupId' column
data['groupId'] = np.random.randint(1, 6, 100)

# Populate columns with suffix 'f' (float values)
for col in columns:
    if col.endswith('f'):
        data[col] = np.random.randint(1,100,100)

# Populate columns with suffix 'v' (integer values)
for col in columns:
    if col.endswith('v'):
        data[col] = np.random.randint(1, 100, 100)

# Create a DataFrame
df_result = pd.DataFrame(data)

# Write to csv
df_result.to_csv('random_data_with_names.csv', index=False)
