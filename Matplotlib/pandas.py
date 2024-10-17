import pandas as pd

data = {
    'Name': ['Jack', 'Robert', 'John', 'Smith'],
    'Age': [30, 25, 40, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
}

df = pd.DataFrame(data)
print(df)
