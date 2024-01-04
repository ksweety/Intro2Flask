import pymysql
import pymysql.cursors

con = pymysql.connect(host = '10.100.33.60',
                             user='kwilliams4',
                             password='228426581',
                             database='world', 
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)  

cursor = con.cursor()
cursor.execute("SELECT `Name` FROM `country`" ) 

results = cursor.fetchall()  

from pprint import pprint as print

print(results)

for x in results: 
    print(x['HeadOfState'])

