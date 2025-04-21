import re
import pandas as pd

file_path = '../.././archive/test-original.csv'

data = []
with open(file_path, 'r', encoding='utf-8') as f:
    current_line = ""
    for line in f:
        line = line.strip()
        if re.match(r'^\d+,', line):
            if current_line:
                data.append(current_line)
            current_line = line
        else:
            current_line += " " + line
    if current_line:
        data.append(current_line)

with open(file_path, 'w', encoding='utf-8') as f:
    for row in data:
        f.write(row + '\n')

df = pd.read_csv(file_path, header=None, names=['tweet_id', 'name', 'attribute', 'text'])
df = df.drop(['name','attribute'], axis=1)
# df = df[df['attribute'].isin(['Positive', 'Negative'])]
# df['attribute'] = df['attribute'].map({'Positive': 1, 'Negative': 0})
df.to_csv(file_path, index=False, header=False)