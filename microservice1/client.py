from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/pagar', methods=['POST'])
def pagar():
    # Simulação do pagamento
    data = request.json

    print(f"Pagamento realizado: {data}")
    
    # Notificando o microserviço 2
    response = requests.post('http://m2:5001/notificar', json=data)
    
    return jsonify({'status': 'Pagamento processado', 'notificacao_status': response.json()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
