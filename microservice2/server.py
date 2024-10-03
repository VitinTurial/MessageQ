from flask import Flask, request, jsonify
import json

app = Flask(__name__)

import boto3

fila = None

def create_sqs_queue():
    sqs = boto3.client(
        'sqs',
        region_name='sa-east-1',
        endpoint_url='http://localhost:4566'  
    )

    response = sqs.create_queue(QueueName='s-de-queue')
    fila = response['QueueUrl']
    return fila

def send_message(queue_url, message_body):
    sqs = boto3.client(
        'sqs',
        region_name='sa-east-1',
        endpoint_url='http://localhost:4566'  
    )
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    return response

@app.route('/notificar', methods=['POST'])
def notificar():
    data = request.json
    
    print(f"Notificação recebida: {data}")
   
    if fila is None:
        return jsonify({'error': 'A fila ainda não foi criada.'}), 500

    response = send_message(fila, message)
    print(f"Mensagem enviada à fila: {response['MessageId']}")

    return jsonify({'status': 'Notificação processada'}), 200

if __name__ == '__main__':
    print(f"Fila criada: {create_sqs_queue()}")
    app.run(host='0.0.0.0', port=5001)