import pandas as pd
df = pd.read_csv('/home/shashank/Desktop/Python/d.csv') 
#df = pd.read_table('')
df.to_excel('output.xlsx', 'Sheet1')
'''
import pandas as pd
df = pd.read_fwf('/home/shashank/Desktop/Python/po_data.txt')
df.to_csv('/home/shashank/Desktop/Python/d.csv')
'''
