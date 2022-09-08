'''
1 . Write a program to insert a record in sql table via api 
2.  Write a program to update a record via api 
3 . Write a program to delete a record via api 
4 . Write a program to fetch a record via api.


Task performed by: Ranjeet Prajapati '''


from logging import exception       
from flask import Flask,request,jsonify
import mysql.connector as conn


app=Flask(__name__)        # making object 'app' of class 'flask'

@app.route('/insert',methods=['GET','POST'])   # decorator use to make the rout for connection
def insert_sql():                               # function for insertion of value in database
    try:
        if(request.method=='POST'):
            mydb=conn.connect(
                        host='localhost',
                        user='root',
                        password='Ranj1296@',
                        
                        )

            mycursor=mydb.cursor()
            name=request.json['name']
            salary=request.json['salary']

            mycursor.execute(f"insert into sanjaydb.rano values('{name}',{salary})")

            mydb.commit()
            return "succesfully inserted"

    except Exception as e:
        print(e)
        return "fail"

@app.route('/update',methods=['GET','POST'])
def update_sql():                   # function for updation of value in database
    try:
        if(request.method=='POST'):
            mydb=conn.connect(
                        host='localhost',
                        user='root',
                        password='Ranj1296@',
                        database='ranjeetdb'
                        )
            mycursor=mydb.cursor()
            clg_id=request.json['id']
            clg_name=request.json['name']
            roll_no=request.json['roll']

            mycursor.execute(f"UPDATE college SET clg_id = {clg_id}, clg_name = '{clg_name}' WHERE roll_no = {roll_no}")

            mydb.commit()
            
            return "succesfully updated"
    except Exception as e:
        print(e)
        return "fail2"


@app.route('/delete',methods=['GET','POST'])
def ranjeetdb_delete():                 # function for deletion of value in database
    try:
        if(request.method=='POST'):
            mydb=conn.connect(
                host='localhost',
                user='root',
                password='Ranj1296@'
            )

            mycursor=mydb.cursor()
            nm=request.json['name']
            

            mycursor.execute(f"DELETE FROM sanjaydb.rano WHERE name='{nm}'")
            mydb.commit()

            return "succesfully deleted"
    except Exception as e:
        print(e)
        return "fail delete operation"

@app.route('/fetch',methods=['GET','POST'])
def fetch():                    # function for fetching the value from database
    try:
        if(request.method=='POST'):
            mydb=conn.connect(
                host='localhost',
                user='root',
                password='Ranj1296@'
            )
            mycursor=mydb.cursor()
            mycursor.execute("select*from sanjaydb.rano")

        l=[]
        for i in mycursor.fetchall():
            l.append(i)
        return jsonify(str(l))
    except Exception as e:
        print(e)
        return "not fetched any data"


if __name__=='__main__':        #use to run the main fuction 
    app.run()

    
        
'''------------***END***---------------'''