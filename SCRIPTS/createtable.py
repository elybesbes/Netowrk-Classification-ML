import mysql.connector as mysql
# Connect to the Database
db = mysql.connect(
    host = "197.26.19.254",
    port = "1406",
    user = "root",
    passwd = "root",
    database = "FlowDatabase"
)
print(db)
cursor = db.cursor()
cursor.execute(" CREATE TABLE ML_PREDECTION( category VARCHAR(50), bidirectional_bytes INT, time TIME, flowID INT PRIMARY KEY AUTO_INCREMENT)")
#show table
print("the network flow table:")
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
#Close connection
db.close()

