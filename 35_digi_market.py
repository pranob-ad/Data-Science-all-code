import pandas as pd

df = pd.read_csv('digital_marketing.csv')
#print('frist 10 entris\n',df.head(10))
#print('last 10 entris\n',df.tail(10))

#df.iloc[How many rows I want to see, How many columns I want to see]
print(df.iloc[:6,0:10])
#print(df.iloc[2:6:2,2:8:2]) #All the rows with adspend
#print(df.iloc[0:11:2,0:11:2]) #All the rows with adspend
#print(df.loc[df['Gender']=='Female',['CustomerID','Gender','Income']])
#print(df.loc[df['Income']< 40000])
#print(df.loc[(df['Income']<40000) & (df['Gender']=='Female'),['CustomerID','Gender','Income']])
#df.loc[0,'Income']= None
#print(df.head(5))
#df['Income'].fillna(df['Income'].median())
#print(df.head)

#Check the adspend in campaingn channel the category wise maximum
df = df.groupby('CampaignChannel')['AdSpend']
print(df.max())
print(df.describe())