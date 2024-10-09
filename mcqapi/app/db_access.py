import sqlite3
import logging
import os 
import json

# SQLlite3 database name
Database = 'MCQ.db'

"""
Establishes a conncetion to the MCQ.db, verifies one of the required table is presnet 
in the Db. If its not present then it would initialize the db with insert.sql

returns : 
    connection to MCQ.db

"""

def get_db_connection():
    cn = sqlite3.connect(Database)
    cn.row_factory = sqlite3.Row
    
    res = cn.execute("SELECT name FROM sqlite_master WHERE name='current_session'")
    
    if res.fetchone() is None :
        file_path = os.path.join(os.curdir,'app','db_init.sql')
        logging.info(file_path)
        with open(file_path) as f : 
            cn.executescript(f.read())
        logging.info("Database is initialized with base schema")
    
    return cn

def select_question_mapper(skill):
    #try:
    cn = get_db_connection() 
    cursor = cn.execute('''SELECT file_name FROM question_mapper WHERE skill = ?''', (skill,))
    res = cursor.fetchone()
    #finally :
    #    cn.close()
    return res[0] if res else None


def fetch_questions(skill) : 
    file_name = select_question_mapper(skill)
    if file_name :
        file_path = os.path.join(os.curdir,'mcqdb', file_name)
        with open(file_path, 'r',encoding='utf-8') as file:
            return json.load(file)
    else :
        return None

def insert_current_session(data):
    try:
        cn = get_db_connection() 
        cursor = cn.cursor()
        cursor.execute('''INSERT INTO current_session(file_name) VALUES (?)''', (json.dumps(data),))
        cn.commit()
        last_id = cursor.lastrowid
        print(f"Data loaded successfully. Loaded ID: {last_id}")
        return last_id 
    except Exception as e : 
        print("Test questions could not be loaded into the db due to",e)
    finally :
        cn.close()

def select_session_data(id):
    #try:
    cn = get_db_connection() 
    cursor = cn.execute('''SELECT file_name FROM current_session WHERE id = ?''', (id,))
    res = cursor.fetchone()
    #finally :
    #    cn.close()
    return res[0] if res else None

        
