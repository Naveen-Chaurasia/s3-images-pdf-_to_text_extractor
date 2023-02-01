import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ardhi"
)

mycursor = mydb.cursor()


sql = "INSERT INTO materials (PART_No, REF_DRG_No,DESCRIPTION,MATERIAL,QTY,UNIT,MASS_Kgs) VALUES (%s, %s,%s,%s,%s,%s,%s)"
val = ('3 ', '', 'CAMLOCK ', 'SS304 ', '1 ', 'NOS ', '1.342 ')
g=mycursor.execute(sql, val)
mydb.commit()  
print(mycursor.rowcount, "record inserted.") 
print(g)  