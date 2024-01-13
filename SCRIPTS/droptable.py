import mysql.connector
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
#drop table
cursor.execute("DROP TABLE IF EXISTS NETWORK_FLOW")
print("Done")
# Close connection
db.close()
