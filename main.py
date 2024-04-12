# Pandas: How to get the Max and Min Dates in a DataFrame

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'salary': [175.1, 180.2, 190.3, 205.4],
    'date': ['2023-01-05', '2023-03-25', '2021-01-24', '2022-01-29']
})

max_date = max(df['date'])
print(max_date)  # 👉️ 2023-03-25

min_date = min(df['date'])
print(min_date)  # 👉️ 2021-01-24