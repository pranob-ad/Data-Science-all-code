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

df["Family"] = df["SibSp"] + df["Parch"]
df["Family"].value_counts()

#which family class type are dominant
print(df[["Pclass", "Family"]].groupby("Pclass").mean())
#age_reference = df[["Sex", "Title","Sex"]].groupby(["Sex","Title"]).mean().reset_index()
#print(age_reference)
sns.histplot(data = df, x = "Age", hue = "Survived")
plt.show()