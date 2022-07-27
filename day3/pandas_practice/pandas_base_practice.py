import pandas as pd

data = {
    'year': [2016, 2017, 2018],
    'GDP rate': [2.8, 3.1, 3.0],
    'GDP': ['1.637M', '1.73M', '1.83M']
}

df = pd.DataFrame(data)

df['year']
# df.year

df[df['year'] > 2016]

sum = df['GDP rate'].sum()
avg = df['GDP rate'].mean()
print("sum : ", sum, "avg : ", avg)
