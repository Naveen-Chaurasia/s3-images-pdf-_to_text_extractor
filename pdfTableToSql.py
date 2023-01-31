import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ardhi"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Ardhi")
#mycursor.execute("CREATE TABLE Materials ( PART_No  VARCHAR(255), REF_DRG_No  VARCHAR(255),DESCRIPTION  VARCHAR(255),MATERIAL VARCHAR(255),QTY VARCHAR(255), UNIT VARCHAR(255),MASS_Kgs VARCHAR(255))")
