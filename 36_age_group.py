import pandas as pd

df = pd.read_csv('digital_marketing.csv')
def age_group(age):
    if age <= 25:
        return "group 1 (0-25)"
    elif 26<=age<=35:
        return 'group 2 (26 - 35)'
    elif 36<=age<=45:
        return 'group 3 (36-45)'
    else:
        return 'group 4 (46+)'
        
df['AgeGroup'] = df['Age'].apply(age_group)
group_age_summary = df.groupby('AgeGroup') [['AdSpend','ConversionRate', 'WebsiteVisits']]
print(group_age_summary.mean())