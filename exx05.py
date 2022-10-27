#5) Qual é a quantidade de assessores?
####################
# importing libraries
import pandas as pd
 
# storing the data of clients in the dictionary
acessor_data = {'acessor': [
'A1 ',
'A2 ',
'A3 ',
'A4 ',
'A4 ',
'A6 ',
'A7 ',
'A8 ',
'A9 ',
'A10',
'A11',
'A10',
'A1 ']}
 
# creating DataFrame for the data using pandas
acessor_df = pd.DataFrame(acessor_data)
 
# finding unique values present in the particular group.
name_count = pd.unique(acessor_df['acessor'])


 
# initializing variable to 0 for counting
name_unique = 0


 
# writing separate for loop of each groups
for item in name_count:
    name_unique += 1
 

 
# printing the number of unique values present in each group
print(f'O número de total acessores, considerando cada um individualmente, é: {name_unique}')
