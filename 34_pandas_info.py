import pandas as pd

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

data=pd.Series([10,20,30],index=['parit_singla','Bhavesh','ritik'])
print(data)

print(data['ritik'])

