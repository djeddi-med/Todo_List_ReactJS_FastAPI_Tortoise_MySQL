from fastapi import FastAPI
import mysql.connector

DB_conn = mysql.connector.connect(
    host='localhost', 
    port='3307',
    user='root', 
    password='', 
    database='todo'
    )

cursor = DB_conn.cursor()

app = FastAPI()

@app.get('/')
def get_all():
    sql = "SELECT * FROM `todo` WHERE 1"
    cursor.execute(sql)
    to_do = cursor.fetchall()
    return to_do

@app.get('/todo')
def get_to_do_avec_id(myid:int):
    sql = "SELECT * FROM `todo`"
    cursor.execute(sql)
    to_do = cursor.fetchall()
    return to_do[0]

@app.delete('/todo/{myid}')
def del_todo(myid:int):
    sql = "DELETE FROM `todo` WHERE id=$s"
    val = (myid,)
    cursor.execute(sql, val)
    DB_conn.commit()
    return 'deleted'


@app.post('/todo/create')
def create_todo(title: dict):
    sql = "INSERT INTO `todo`(`title`, `done`, `create_at`) VALUES ($s, $s, $s)"
    val = (title['title'], title['done'], title['create_at'])
    print(val)
    cursor.execute(sql, val)
    DB_conn.commit()
    return 'Added'

@app.post('/todo/update')
def update_todo(myid:int, title: dict):
    sql = "UPDATE `todo` SET `title`=$s,`done`=$s,`create_at`=$s WHERE $s"
    val = (title['title'], title['done'], title['create_at'], myid)
    cursor.execute(sql, val)
    DB_conn.commit()
    return 'Updated'
