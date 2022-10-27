#2) Qual é custodia total?

##########
import numpy as np
import pandas as pd

#define dataframe and column values
df = pd.DataFrame({
   'custodia' : [60000.00,
 50000.00,
 123000.00, 
 800500.00, 
 800500.00, 
 20000.00,
 40000.00,   
 50000.00,
 100000.00, 
 24242.00, 
 24242.00, 
 24242.00]})
 
#define local total of the column
df.loc['Total'] = df.sum()
print(df)
