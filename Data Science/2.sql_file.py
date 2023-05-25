import mysql.connector
import pandas as pd

conn = mysql.connector.connect(host="localhost", username="root", password="Shahil@1999")

p1 = pd.read_sql_query("SELECT * FROM world.city;", conn)
print(p1)

p = pd.read_sql_query("SELECT * FROM world.city where CountryCode like 'IND';", conn)

print(p)

