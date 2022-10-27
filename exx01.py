#1) Qual a quantidade de clientes diferentes na base de dados?
####################
# importing libraries
import pandas as pd
 
# storing the data of clients in the dictionary
client_data = {'Nome do Cliente': [
'João',
'Walter',
'Daniel',
'Matheus',
'Matheus',
'José',
'Tiago',
'Lourenço',
'Marina',
'Thaís',
'Juliana',
'Mario',
'Marcio'],
             
'codigocliente': [
1,
2,
3,
4,
4,
5,
6,
7,
8,
9,
10,
11,
12
]}
 
# creating DataFrame for the data using pandas
client_df = pd.DataFrame(client_data)
 
# finding unique values present in the particular group.
name_count = pd.unique(client_df['Nome do Cliente'])
codigocliente_count = pd.unique(client_df.codigocliente)

 
# initializing variable to 0 for counting
name_unique = 0
codigocliente_unique = 0

 
# writing separate for loop of each groups
for item in name_count:
    name_unique += 1
 
for item in codigocliente_count:
    codigocliente_unique += 1

 
# printing the number of unique values present in each group
print(f'O número de cliente  únicos é: {name_unique}')
print(f'O número de códigos de clientes únicos é: {codigocliente_unique}')
