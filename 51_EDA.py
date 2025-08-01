import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

#missing_vlu= df.isnull().sum()
#print(missing_vlu)
#print(df.describe())
#df.drop(columns=['PassengerId','Ticket'], inplace=True)

# Save the modified DataFrame back to the CSV file (overwrite original)
#df.to_csv('train.csv', index=False)

#print(df[['Survived','Pclass','Age','SibSp','Parch','Fare', 'Embarked']].apply(pd.unique))
#print(df['Survived'].value_counts())
#print(df['Pclass'].value_counts())
#print(df['Age'].value_counts())
#print(df['Parch'].value_counts())
#print(df['sibsp'].value_counts())
#print(df['Fare'].value_counts())
#print(df['Embarked'].value_counts())


#now visualize things
"""
sns.boxplot(df['Age'])
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title("Fare Distribution by Class")
sns.boxplot(x='Embarked', y='Fare', data=df)
plt.title('Fare Distribution by Embarkation Port')
sns.PairGrid(df,hue='Pclass').map(sns.boxplot)
plt.title("all posible box plot")
sns.countplot(x='Survived',data=df, hue="Pclass")
plt.title('counting survival class wise')
"""
'''
df_survive= df[["Pclass", "Survived"]].groupby("Pclass").mean().reset_index()
df_survive[["Survived"]]= df_survive[["Survived"]]*100
print(df_survive)
df_survive.rename(columns={"Survived": "Survived in %"}, inplace=True)
sns.barplot(x= 'Pclass',y='Survived in %',data=df_survive)
'''

sns.barplot(x= 'Sex',y='Survived',data=df, hue='Pclass')
plt.show()

