import pandas as pd
import os 
from flask import Flask, render_template, request, redirect, url_for, abort
import pyodbc as ODBC
from os import environ



app = Flask(__name__)


#create connection
conn = ODBC.connect( 
   'DRIVER={ODBC Driver 17 for SQL Server};'
   'SERVER=*****;'
   'Database=*****;'
   'UID=******;'
   'PWD=******;'
    
  )

cursor = conn.cursor()

@app.route('/', methods=['GET', "POST"])
def index():
#    tables = ["blast","blast2"]
#    if request.method == "GET":
#        return render_template("index.html", tables=tables)
#    elif request.method == "POST":
#        return render_template("result.html", table=request.form.get("table"))
#    else:
#        abort(404)
    return render_template('index.html')
   



@app.route('/', methods=['GET' , 'POST'])
def UPLOAD():
     current = os.getcwd()
     if request.method == 'POST':
        uploaded_file = request.files['file']
        file_path = os.path.join(current, uploaded_file.filename)
        uploaded_file.save(file_path)
        checkCSV(file_path)
        return redirect(url_for('page2'))   

stmt = "select * from *****.INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'blast2'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    #@app.route('/', methods=['POST'])
    def checkCSV(filePath):
        
        col_names = ['FirstName', 'LastName', 'Email', 'PlayerID']
        csvdata = pd.read_csv(filePath,names=col_names, header = None, lineterminator='\n')
        for i,row in csvdata.iterrows():
            cursor.execute('''
                    INSERT INTO blast2 (FirstName, LastName, Email, PlayerID )
                    VALUES (?, ?, ?, ?)
                    ''',
                    row.FirstName,
                    row.LastName,
                    row.Email,
                    row.PlayerID
                    )
            conn.commit()

    @app.route('/page2')#, methods=['GET' , 'POST'])
    def page2():
        return render_template('page2.html')
else:

    #create table
    cursor.execute( 
        ''' 
                CREATE TABLE blast2(
                    LastName varchar(50),
                    FirstName varchar(50),
                    Email varchar(50),
                    PlayerID varchar(100) primary key
                )
        '''
    )
    conn.commit()
    #def checkCSV(filePath):
        #col_names = ['FirstName', 'LastName', 'Email', 'PlayerID']
        #csvdata = pd.read_csv(filePath,names=col_names, header = None, lineterminator='\n')
        #for i,row in csvdata.iterrows():
            #cursor.execute('''
                    #INSERT INTO blast2 (FirstName, LastName, Email, PlayerID )
                    #VALUES (?, ?, ?, ?)
                    #''',
                    #row.FirstName,
                    #row.LastName,vhjgjn
                    #row.Email,
                    #row.PlayerID
                    #)
            #conn.commit()

    @app.route('/page2')#, methods=['GET' , 'POST'])
    def page2():
        return render_template('page2.html')



app.config["DEBUG"] = True

if __name__ == '__main__':
   app.run(port = 5000)





