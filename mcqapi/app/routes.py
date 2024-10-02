from flask import Blueprint, request,jsonify
import app.controllers as controllers 

main = Blueprint('main',__name__)

@main.route('/test', methods=['GET'])
def test():
    skill = request.args.get('skill')
    if not skill : 
        return {"error":"skill parameter is required"}, 400
    return controllers.fetch_test(skill)

@main.route('/result', methods=['GET'])
def result():
    data = request.get_json()
    print(data)
    if data is None:
        return {"error": "Invalid JSON or missing content"}, 400
    return controllers.fetch_result(data)