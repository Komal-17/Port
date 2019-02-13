import pymysql
connection = pymysql.connect(host="localhost" , user="root" , password=" " , database="portfolio")
cursor = connection.cursor()

connection.commit()
connection.close()