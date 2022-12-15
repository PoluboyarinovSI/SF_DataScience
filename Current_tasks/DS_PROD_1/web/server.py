import pickle
import numpy as np

from flask import Flask, request, jsonify

# Загружаем модель из файла
with open('models/model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)


# Создаем приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Test message. The server is running"
    return msg


@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json)
    features = np.array(features).reshape(1, 4)
    
    prediction = model.predict(features)
    
    return jsonify({
        'prediction': prediction[0]
    })


if __name__ == '__main__':
    app.run('localhost', 5000) 