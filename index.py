# A biblioteca "dotenv" é possui a função "load_dotenv()" que
# é usada para carregar o arquivo .env com as chaves da API
# do X. O arquivo .env é usado para manter os segredos das
# chaves.
from dotenv import load_dotenv
# a biblioteca "os" possui o método ".getenv" que pega do
# arquivo .env as variaveis com os valores das chaves
# atribuidos.
import os
# a biblioteca tweepy é usada para conectar com a API do X
# através das chaves do arquivo .env
import tweepy as tw
# o textblob é uma biblioteca utilizada fazer a analise de
# sentimento do tweet.
from textblob import TextBlob

# carrega as varaiveis de ambiente a partir
# do arquivo .env
load_dotenv() 
# Obtém o Bearer Token da variável de ambiente
bearer_token = os.getenv("BEARER_TOKEN")

# Cria o cliente da API do X para permitir fazer
# solicitaçoẽs à API.
api = tw.Client(bearer_token)
# Define a palavra chave de pesquisa.
query = 'palavra_chave_aqui'
# Busca os tweets mais recentes contendo a palavra-chave
# e defini o numero mais de resultados a 10.
search_results = api.search_recent_tweets(query, max_results=10)
# extrai o texto de cada tweet e coloca em uma lista.
tweets = [tweet.text for tweet in search_results.data]

# Para cada tweet na lista de tweets, é criado um objeto
# TextBlob.
for tweet in tweets:
    blob = TextBlob(tweet)
    # imprime o tweet
    print(tweet)
    #imprime o sentimento do tweet com base em sua polaridade.
    if blob.sentiment.polarity < 0 :
        print("negative")
    elif blob.sentiment.polarity > 0 :
        print("positive")
    else:
        print("neutral")
    
        
    
