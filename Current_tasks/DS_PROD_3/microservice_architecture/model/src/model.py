import pika
import pickle
import json
import numpy as np

with open('./myfile.pkl', 'rb') as pkl_file:
    regressor = pickle.load(pkl_file)

try:
    # Подключение к серверу
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Указание с какой очередью работаем
    channel.queue_declare(queue='features')

    # Создаём очередь y_pred
    channel.queue_declare(queue='y_pred')

    def callback(ch, method, properties, body):
        print(f'Получен вектор признаков {body}')
        features = json.loads(body)
        shaped_features = np.array(features).reshape(1, -10)
        pred = regressor.predict(shaped_features)
        # Публикуем сообщение
        channel.basic_publish(exchange='',
                            routing_key='y_pred',
                            body=json.dumps(pred[0]))
        print('Предсказание {prediction} отправлено в очередь y_pred')


    # Извлекаем сообщение из очереди features
    # on_message_callback показывает, какую функцию вызвать при получении сообщения
    channel.basic_consume(
        queue='features',
        on_message_callback=callback,
        auto_ack=True
    )
    print('...Ожидание сообщений, для выхода нажмите CTRL+C')

    # Запускаем режим ожидания прихода сообщений
    channel.start_consuming()
except:
    print('Не удалось подключиться к очереди')
