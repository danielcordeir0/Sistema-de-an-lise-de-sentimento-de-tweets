# Twitter Sentiment Analysis System

Este projeto realiza a análise de sentimentos de tweets utilizando a API do Twitter (agora chamada de X) e a biblioteca TextBlob. O sistema busca tweets recentes contendo uma palavra-chave específica e analisa o sentimento de cada tweet.

## Funcionalidades

- Conectar-se à API do X usando a biblioteca tweepy.
- Buscar tweets recentes contendo uma palavra-chave.
- Analisar o sentimento dos tweets utilizando a biblioteca TextBlob.

## Requisitos

- Python 3
- Conta no Twitter com acesso à API (necessário para obter as chaves da API)

## Bibliotecas Necessárias

- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [tweepy](https://docs.tweepy.org/en/stable/)
- [textblob](https://textblob.readthedocs.io/en/dev/)


## Instalação das bibliotecas

```
pip install tweepy textblob python-dotenv
```
## Configuração

### Clonar o Repositório:
```
git clone https://github.com/danielcordeir0/Sistema-de-an-lise-de-sentimento-de-tweets.git
```
### Alterar o arquivo .env
Entre no arquivo .env e adicione seu bearer token, fornecido pela API do X:
```
BEARER_TOKEN=seu_bearer_token_aqui
```
### Definir query:
No arquivo index.py defina sua query adicionando a palavra-chave:
```
query = 'palavra_chave_aqui'

```
## Como Funciona
1. **Carregamento de Variáveis de Ambiente:** O script carrega as variáveis de ambiente a partir de um arquivo `.env` usando a biblioteca dotenv.
2. **Autenticação na API do X:** Utiliza o `bearer_token` para autenticar as requisições na API do X usando Tweepy.
3. **Busca de Tweets:** Realiza uma busca por tweets recentes contendo a palavra-chave especificada (`query`).
4. **Análise de Sentimento:** Para cada tweet encontrado, o script cria um objeto TextBlob e imprime o tweet e seu sentimento (positivo, negativo ou neutro).

## Observações
- Certifique-se de que seu arquivo .env está corretamente configurado com suas credenciais da API do Twitter.
