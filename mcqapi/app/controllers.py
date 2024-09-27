import app.db_access as db
from flask import jsonify
import logging
import random 


def fetch_test(skill):
    quests = db.fetch_questions(skill)
    logging.info(quests)
    if quests is None or quests == 0 or len(quests) < 5 :
        return jsonify({"error":"need minimum of 5 questions in JSON file to fetch questions"})
    else : 
        res_quests = random.sample(quests,5)
        id = db.insert_current_session(res_quests) # fetch the id for the questions
        return jsonify({id:res_quests}) 



         