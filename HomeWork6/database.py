import pandas as pd
import sqlite3

from matplotlib.pyplot import connect
from sympy import pprint

presents = pd.read_csv('presents.csv')
#print(presents.head())
connection = sqlite3.connect('presents.db')

presents.to_sql('presents', connection, index = False, if_exists= 'replace')

sql = '''
    SELECT * from presents;
'''

output = pd.read_sql(sql, connection)
print(type(output))
print(output)