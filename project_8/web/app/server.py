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
            return 'No input data'
        else:
            visitorid = request.args.get("visitorid")
            if visitorid is None:
                return "incorrect query parameter. Correct is '/?visitorid=...'"
            if not visitorid.isnumeric():
                return 'Incorrect visitorid. Numeric only!'
            visitorid = int(visitorid)
            if visitorid is None:
                return "No visitorid input data"

            if not user_checker(visitorid):
                return "Wrong visitorid!"

            recommendations = get_predictions(visitorid)
            recommendations = [str(rec) for rec in recommendations]
            recommendations_str = ", ".join(recommendations)

            response = f"""
            visitorid is {visitorid}, recommended itemids: {(recommendations_str)}
            """
            return response
    else:
        return "<h1>No data in GET request</h1>"

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
            recomm_json = {"recommendations": recommendations}
            return json.dumps(recomm_json)
    else:
        return []


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)