import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')
def replc_title(row):
    title= row["Title"]
    relavent_titles= ['Mr', 'Mrs', 'Miss', 'Master', 'Dr']
    if title in relavent_titles:
        return title
    else:
        return "others"
df['Title']= df.apply(replc_title, axis=1)
#findjout the relavant columns and find out how many members are the
# in family and plot a graph of which category famity survived most
df["Family"] = df["SibSp"] + df["Parch"]
print(df["Family"].value_counts())
sns.barplot(data = df[["Family", "Survived"]].groupby("Family").mean().reset_index(), x = "Family", y = "Survived")
print(pd.crosstab(df['Title'], df['Family']))
plt.show()