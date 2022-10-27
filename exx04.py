#4) Qual a media de idade de todos os clientes?

########

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'nome cliente' : ['João    ' ,
'Walter  ' ,
'Daniel  ' ,
'Matheus ' ,
'Matheus ' ,
'José    ' ,
'Tiago   ' ,
'Lourenço' ,
'Marina  ' ,
'Thaís   ' ,
'Juliana ' ,
'Mario   ' ,
'Marcio  '
        ],
    
    
    
   'idade' : [30,
25,
19,
44,
44,
42,
31,
55,
21,
20,
20,
20,
20]})


df.loc['Idade'] = df.mean()
print(df)
