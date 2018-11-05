import csv
import pandas as pd 
'''
df = pd.read_csv('Indian_names_dataset.csv')
df_names_list = df['name_m'].tolist()

df_names_list = list(set(df_names_list))
print (len(df_names_list))
df_female_names_list = df['name_f'].tolist()
df_female_names_list = list(set(df_female_names_list))
print (len(df_female_names_list))
#print (len(df_female_names_list))
for i in df_female_names_list:
    df_names_list.append(i)
print (len(df_names_list))
'''
    
#df_gender_list = df['gender_m'].tolist()
#df_female_gender_list = df['gender_f'].tolist()
#for i in df_female_gender_list:
    #df_gender_list.append(i)
df1 = pd.read_csv('Indian_names_dataset_final.csv')
#df1['names'] = pd.Series(df_names_list)
#df1['gender'] = pd.Series('male',size = 8520)
#df1 = df1.dropna()
#print (len(df1['names']))
df1 = df1.sample(frac=1)
df1['gender'] = pd.Categorical(df1['gender'])
#print (df1)
df1.to_csv('Indian_names_dataset_final1.csv', encoding='utf-8')


