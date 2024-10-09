import app.db_access as db
from flask import jsonify
import logging
import random 
from flask import request
import json 


def fetch_test(skill):
    quests = db.fetch_questions(skill)
    logging.info(quests)
    if quests is None or quests == 0 or len(quests) < 5 :
        return jsonify({"error":"need minimum of 5 questions in JSON file to fetch questions"}), 404
    else : 
        res_quests = random.sample(quests,5)
        id = db.insert_current_session(res_quests) # fetch the id for the questions
        return jsonify({'testId':id,'quests':res_quests}) 


def fetch_result(data):
    test_data = db.select_session_data(data['testid'])
    test_data_json = json.loads(test_data)
    user_answers = {option['id']: option['answerKey'] for option in data['options']}
    result = 0
    
    for item in test_data_json :
        item['userAnswer']=user_answers[item['id']]
        if item['userAnswer'] == item['answerKey'] :
            item['result'] = 0
            result = result + 1
            del item['answerKey']
        else : 
            item['result'] = 1
            
    return jsonify({'result':result,'quests':test_data_json})

#
    
    
    