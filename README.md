# Integração com API da RD Station

Este projeto consiste em utilizar e interagir com a API da RD Station. 

## Sumário
1. [Pré-requisitos](#pré-requisitos)
2. [Configuração do Ngrok](#configuração-do-ngrok)
3. [Criando um aplicativo na RD Station](#criando-um-aplicativo-na-rd-station)
4. [Gerando o código de autorização](#gerando-o-código-de-autorização)
5. [Obtendo o access token](#obtendo-o-access-token)
6. [Exemplo de uso](#exemplo-de-uso)

## Pré-requisitos

- Conta na RD Station
- Conta no Ngrok
- Python instalado
- Pacotes `Flask`, `pyngrok` e `requests` instalados

## Configuração do Ngrok

### Parte 1: Criando uma conta no Ngrok

1. Acesse [Ngrok](https://ngrok.com/)
2. Crie ou entre em uma conta
3. No canto superior esquerdo, clique em "Your Authtoken" e copie o token gerado

### Parte 2: Instalando e configurando Ngrok

1. Visite a [página de download do Ngrok](https://ngrok.com/download) e baixe o arquivo zip correspondente ao seu sistema operacional.
2. Extraia o Ngrok para um diretório de sua escolha (por exemplo, `C:\ngrok` no Windows ou `/usr/local/bin` no Linux).
3. Adicione o diretório do Ngrok ao PATH do sistema:
   - **Windows**:
     1. Clique com o botão direito em "Meu Computador" ou "Este PC" e selecione "Propriedades".
     2. Clique em "Configurações avançadas do sistema".
     3. Clique no botão "Variáveis de Ambiente".
     4. Em "Variáveis do sistema", encontre a variável "Path" e clique em "Editar".
     5. Adicione o caminho do diretório onde o Ngrok foi extraído (por exemplo, `C:\ngrok`).
     6. Clique em "OK" para fechar todas as janelas.

### Gerando URL de Callback

Crie um arquivo Python (por exemplo, `gerarCallback_Code.py`) e cole o código abaixo:

```python
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
    ngrok.set_auth_token("TOKEN_DO_NGROK")  # ALTERE TOKEN_DO_NGROK PELO TOKEN FORNECIDO NO SITE DO NGROK
    http_tunnel = ngrok.connect(5000)
    print("Public URL:", http_tunnel.public_url)
    app.run(port=5000)
```

Execute o código acima e obtenha a URL fornecida no terminal. **Deixe o código sendo executado**, pois a cada nova execução será gerada uma nova URL.

## Criando um aplicativo na RD Station

1. Acesse a [App Store da RD Station](https://appstore.rdstation.com/pt-BR/publisher) e faça login.
2. Clique em "Quero criar um aplicativo", escreva o nome do seu aplicativo e escolha a opção "Aplicativo privado". Clique em "Criar app".
3. Preencha os campos e em URL Callback coloque a URL fornecida pelo Ngrok.
4. Clique em "Salvar" e copie a chave do "Client ID" e "Client Secret".

## Gerando o código de autorização

1. Componha a URL de autorização substituindo os parâmetros `client_id` e `redirect_uri` pelas credenciais obtidas no passo anterior:
   ```
   https://api.rd.services/auth/dialog?client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&state=state
   ```
   Exemplo:
   ```
   https://api.rd.services/auth/dialog?client_id=1111111111111&redirect_uri=https://suaURLdeCallback&state=state
   ```
2. Acesse a URL no navegador, continue e conecte. Após isso, vá ao terminal do código que está sendo executado e copie o "code" fornecido.

## Obtendo o Access Token

Crie um novo arquivo Python (por exemplo, `gerarToken.py`) e cole o código abaixo substituindo `client_id`, `client_secret` e `code`:

```python
import requests

url = 'https://api.rd.services/auth/token?token_by=code'
headers = {
    'accept': 'application/json',
    'content-type': 'application/json'
}
data = {
    "client_id": "INSIRA_SEU_CLIENT_ID",
    "client_secret": "INSIRA_SEU_CLIENT_SECRET",
    "code": "INSIRA_CODE"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

Execute o código acima em um novo terminal. **Mantenha a execução do código URL Callback**.

Após executar o código, será exibido no terminal `access_token` e `refresh_token`. Copie o `access_token`.

## Exemplo de uso

### Exibindo dados dos contatos de uma segmentação específica

1. Acesse a segmentação de leads no RD Station e copie o ID da segmentação da URL:
   ```
   Exemplo: https://app.rdstation.com.br/segmentation/edit/13222999
   ```

2. Crie um arquivo Python e cole o código abaixo substituindo `access_token`:

```python
import requests

url = "https://api.rd.services/platform/segmentations/13222999/contacts"

headers = {
    "accept": "application/json",
    "authorization": "Bearer INSERIR_ACCESS_TOKEN"
}

response = requests.get(url, headers=headers)

print(response.text)
```

### Referências

- [Autenticação - RD Station](https://developers.rdstation.com/reference/autentica%C3%A7%C3%A3o)
- [Criar aplicativo na Appstore](https://developers.rdstation.com/reference/criar-aplicativo-appstore)
- [Gerar Code](https://developers.rdstation.com/reference/gerar-code)
- [Obter Tokens de Acesso](https://developers.rdstation.com/reference/obter-tokens-acesso)
- [Atualizar Access Token](https://developers.rdstation.com/reference/atualizar-access-token)
