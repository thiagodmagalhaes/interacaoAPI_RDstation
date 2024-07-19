from flask import Flask, request
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/')
def index():
    return "Página iniciada com sucesso!"

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    # Processar o callback aqui
    return "Callback recebido", 200

if __name__ == '__main__':
    # Autentica o ngrok com seu token de autenticação
    ngrok.set_auth_token("2jNOE6WpUW1yCEZK0KDHRuOlN3X_44Q95XsbL2229vD2FL8wd")

    # Inicia um túnel para o servidor local na porta 5000
    http_tunnel = ngrok.connect(5000)
    print("Public URL:", http_tunnel.public_url)

    # Inicia o servidor Flask
    app.run(port=5000)
