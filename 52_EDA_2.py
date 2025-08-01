import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

#the salutation(ex- mr., Miss, Mrs) for each person
df["Title"] = df["Name"].str.extract(' ([A-Za-z]+)\.')
#print(df['Title'].unique())
#print(df['Title'].value_counts())

def replc_title(row):
    title= row["Title"]
    relavent_titles= ['Mr', 'Mrs', 'Miss', 'Master', 'Dr']
    if title in relavent_titles:
        return title
    else:
        return "others"
# Save the modified DataFrame back to the CSV file (overwrite original)
df.to_csv('train.csv', index=False)

    
df['Title']= df.apply(replc_title, axis=1)
#print(df['Title'].unique())
#print(df['Title'].value_counts())

#avg of miss
print(df[df["Title"]=="Miss"]["Age"].mean())
sns.countplot(x="Title", hue="Survived",data=df)
print(pd.crosstab(df['Title'], df['Sex']))
'''
plt.figure(figsize=(8, 5))
sns.countplot(data=df[df['Survived'] == 1], x='Title')
plt.title('Survivors by Title')
plt.xlabel('Title')
plt.ylabel('Number of Survivors')
# plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.show()
'''

plt.show()