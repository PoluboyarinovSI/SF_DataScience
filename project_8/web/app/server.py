import pickle
import json
import numpy as np

from predictor import user_checker, get_predictions
from flask import Flask, request

# объявление сервера
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        params = request.args
        if not len(params):
            return "Не введен идентификатор пользователя. Введите запрос в следующем виде '/?visitorid=...'"
        else:
            visitorid = request.args.get("visitorid")
            
            if visitorid is None:
                return "Неверное значение идентификатора пользователя. Введите запрос в следующем виде '/?visitorid=...'"
            
            if not visitorid.isnumeric():
                return 'Неверное значение идентификатора пользователя - принимаются только численные значения'
            
            visitorid = int(visitorid)
            
            if visitorid is None:
                return "Не введен идентификатор пользователя"

            if not user_checker(visitorid):
                return "Идентификатор пользователя не найден"

            recommendations = get_predictions(visitorid)
            recommendations = [str(rec) for rec in recommendations]
            recommendations_str = ", ".join(recommendations)
            response = f'Для пользователя с идентификатором: {visitorid}, рекомендованы следующие товары: {(recommendations_str)}'
           
            return response
    else:
        return 'Данные в запросе отсутствуют'

# реализация END-Point
@app.route('/recomendations/', methods=['GET'])
def recomm():
    if request.method == 'GET':
        params = request.args
        if not len(params):
            return []
        else:
            visitorid = request.args.get("visitorid")
            if visitorid is None or not visitorid.isnumeric():
                return []
            visitorid = int(visitorid)
            if visitorid is None:
                return []
            if not user_checker(visitorid):
                return []
            recommendations = [int(rec) for rec in get_predictions(visitorid)]
            rec_json = {"recommendations": recommendations}
            return json.dumps(rec_json)
    else:
        return []


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)