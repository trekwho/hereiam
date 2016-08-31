import pandas as pd

data = pd.read_csv('30people_new.csv',encoding='utf-8')

#replace column name for different results
by_group = data.groupby(data['rating'])
group_sum = by_group.sum()
#print(group_sum)

#for attitudes with conditions, such as identity or location
with_identity = data[data['identity'] == '中共党员']
new_group = with_identity.groupby(with_identity['must'])
#print(new_group.sum())

#for mean and median point in choosing films
mean = data.mean()
median = data.median()
print(median)
