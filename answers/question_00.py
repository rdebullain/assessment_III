import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

"""
Write a function that takes dataframe df (defined above) and string with animal as inputs and returns rows where animal is equal to string (parameter function) and age is less than 3.

Notes:
        - Return empty DataFrame if wrong animal is written
"""

def filter_animals(df,animal):
    # Check if the animal exists in the DataFrame
    if animal not in df['animal'].unique():
        return pd.DataFrame()  # Return empty DataFrame if the animal is not found
    
    # Filter the DataFrame based on the given animal and age less than 3
    filtered_df = df[(df['animal'] == animal) & (df['age'] < 3)]
    
    return filtered_df

# Example usage:
result = filter_animals(df, 'cat')
print(result)