import pandas as pd

data = pd.read_csv('Berkeley.csv')
total_freq=(data['Freq'].sum())

# Solution 2 : Total percent of male/females admitted and rejected.
'''
- Total Male - Admitted Male = Rejected Male
- Total - Total male = Total Female
- Total Female - Admitted Female = Rejected Female
'''

#Total_Male
total_male = ( (data[data['Gender']=='Male']).Freq.array )
male_freq = 0
for i in total_male:
    male_freq += i


#Admitted_Male
male_entry_admitted = (data[ (data['Gender']=='Male') & (data['Admit']=='Admitted') ])

male_admitted_freq = 0
for i in (male_entry_admitted.Freq.array):
    male_admitted_freq += i
# print(male_admitted_freq)

admitted_male_percent = (male_admitted_freq*100)/total_freq
rejected_male_percet = ((male_freq-male_admitted_freq)*100)/total_freq
print("Admitted Male Percent is : "+str(round(admitted_male_percent,2))+"%.")
print("Rejected Male Percent is : "+str(round(rejected_male_percet,2))+"%.")

# total_female
female_freq = total_freq - male_freq
# print(female_freq)

# admitted female
female_entry_admitted = (data[ (data['Gender']=='Female') & (data['Admit']=='Admitted') ])
# print(female_entry_admitted)

female_admitted_freq = 0
for i in (female_entry_admitted.Freq.array):
    female_admitted_freq += i
# print(female_admitted_freq)

admitted_female_percent = (female_admitted_freq*100)/total_freq
rejected_female_percet = ((female_freq-female_admitted_freq)*100)/total_freq
print("Admitted Female Percent is : "+str(round(admitted_female_percent,2))+"%.")
print("Rejected Female Percent is : "+str(round(rejected_female_percet,2))+"%.")