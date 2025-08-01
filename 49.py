import seaborn as sns
import matplotlib.pyplot as plt


#data2 = sns.load_dataset('titanic')
#sns.histplot(data=data2, x= 'age', kde=True, hue= 'class')

data = sns.load_dataset('diamonds')
sns.violinplot(data=data, x='color', y='price', palette='coolwarm')
plt.title("kya bolu mai")

plt.show()