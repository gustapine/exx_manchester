#3) Qual a custodia media?

import numpy as np
import pandas as pd

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


df.loc['Média'] = df.mean()
print(df)
