import pandas as pd


def similarity(n):
    try:
        score = df['second'].value_counts()[n]
    except:
        score = 0
    return n * score

df = pd.read_csv('aoc_1.csv', delimiter='   ', header=None, names=['first', 'second'], engine='python')
df.reset_index()

df_first = df['first'].sort_values().reset_index(drop=True)
df_second = df['second'].sort_values().reset_index(drop=True)
df['first'] = df_first
df['second'] = df_second
df['distance'] = abs(df['first'] - df['second'])
print(df.head())
total_distance = df['distance'].sum()
print(total_distance)

df['similarity_score'] = df['first'].map(similarity)

total_similarity = df['similarity_score'].sum()

print(total_similarity)