import pandas as pd

data = pd.read_csv('Berkeley.csv')
total_freq=(data['Freq'].sum())

# solution 3C : Total percent of male/femal admitted/rejected from each department.
'''
- Admit : Male : A : Freq (Output in percent)
- Reject : Male : A : Freq (Output in percent)
'''

list_admit = (data.Admit).array
len_list = range(len(list_admit))
list_dept =  (data.Dept).array
list_gender = (data.Gender).array

list_freq = list(dict.fromkeys((data.Freq).array))

val = (data.values)
for i in val:
    print(str(i[0]) +' '+ str(i[1]) +' from Dept.'+ str(i[2])+' '+' are '+str(round(((i[3]*100)/total_freq),2))+'%.')