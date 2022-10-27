#6) Qual a custódia total por assessor?
##
# importing pandas as pd
import pandas as pd
  
# creating the dataframe using pandas DataFrame
df = pd.DataFrame({'acessores':['A1','A2','A3','A4','A6','A7','A8','A9','A10','A11'],
                   'Y':[60000,50000, 123000, 800500, 20000, 40000, 0, 50000,100000, 24242],
                   'Z':[ 24242,0,0,800500,0,0,0,0,24242,0]
    
})
  
df['   Soma'] = df.loc[1 : 9,['Y' , 'Z']].sum(axis = 1)
print(df)
