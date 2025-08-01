import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips") #pre loaded data is tips

#sns.barplot(x ='tip', y='total_bill', data = data,hue='sex')
#plt.title("Total Bill vs Tip")


sns.histplot(data= data, x= 'total_bill',hue = 'sex' , kde = True, multiple='stack')
plt.title("Total bill vs Day")
plt.show()

plt.show()