import pandas as pd

data = pd.read_csv('Berkeley.csv')
total_freq=(data['Freq'].sum())

# Solution 1 : Total percent of students admitted and rejected.

admitted_entry = data[data['Admit']=='Admitted']
admitted_freq= 0
for i in admitted_entry:
    b = (admitted_entry['Freq'].tolist())
for j in b:
    admitted_freq += j


admitted_percent = (admitted_freq*100)/total_freq
rejected_percet = ((total_freq-admitted_freq)*100)/total_freq
print("Admitted Percent would be : "+str(round(admitted_percent,2))+"%.")
print("Rejected Percent would be : "+str(round(rejected_percet,2))+"%.")