import mysql.connector as mysql
# Connect to the Database
db = mysql.connect(
    host = "197.26.19.254",
    port = "1406",
    user = "root",
    passwd = "root",
)
cursor = db.cursor()
#Create database
cursor.execute("CREATE database FlowDatabase")
#List databases
print("List of databases : ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())
#close connection
db.close()
