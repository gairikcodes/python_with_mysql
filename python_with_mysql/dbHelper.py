import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost",  port='3306',user="root",password="system", database="my_db")
        query ='create table if not exists user(id int primary key ,userName varchar(20), phNumber varchar(12))'
        
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")
        
    #Insert data 
    def insert_user(self, id, name, phNumber):
        query='insert into user(id,userName,phNumber) values(%s,%s,%s)'
        cur = self.con.cursor()
        values = (id, name, phNumber)
        cur.execute(query, values)
        self.con.commit() #uses python database API to commit the transcation
        #cur.execute("commit")
        print("Inserted")
        
    #Fetch all data 
    def fetch_all(self):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(f"Id: {row[0]}, Name: {row[1]}, Phone Number: {row[2]}")
            
    #delete data
    def delete_user(self, id):
        query='delete from user where id = %s'
        cur=self.con.cursor()
        values = (id,)
        cur.execute(query, values)
        self.con.commit()
        print("Deleted")
        
    #Update data
    def update_user(self, id, name, phNumber):
        query='update user set userName=%s, phNumber=%s where id=%s'
        cur=self.con.cursor()
        values = (name, phNumber, id)
        cur.execute(query, values)
        self.con.commit()
        print("Updated")
    