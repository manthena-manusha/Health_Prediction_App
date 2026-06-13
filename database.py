import oracledb

conn = oracledb.connect(
    user="system",
    password="YOUR_PASSWORD",
    dsn="localhost/XEPDB1"
)

cursor = conn.cursor()

cursor.execute("""
SELECT * FROM patients
""")

for row in cursor:
    print(row)

conn.close()