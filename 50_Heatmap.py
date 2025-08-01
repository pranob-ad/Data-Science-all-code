import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

data = sns.load_dataset('titanic')
num_features= data.select_dtypes(include=np.number).columns
correlation_data = data[num_features].corr()

sns.heatmap(correlation_data, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()