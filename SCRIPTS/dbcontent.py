import mysql.connector as mysql
#Connect to the database
db = mysql.connect(
    host = "197.26.19.254",
    port = "1406",
    user = "root",
    passwd = "root",
    database = "FlowDatabase"
)
print(db)
cursor = db.cursor()
cursor.execute("SELECT * FROM NETWORK_FLOW")
records = cursor.fetchall()
print("Total number of rows in the table : ", cursor.rowcount)
print("\n Printing each row: ")
for row in records :
    print("flow ID", row[3])
    print("time", row[2])
    print("debit", row[4])
    print("application_name", row[0])
    print("application_category_name", row[1], "\n" )

#Close connection
db.close()


