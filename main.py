import tweepy
import keys
import mensagem

#MÉTODO ANTIGO
"""
def api(): #comandos necessários para se conectar ao servidor do twitter
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str): # função que faz o tweet 
    api.update_status(message)   #tweeta a mensagem
    print('tweeted successfully!') #teste de que tudo funcionou como deveria 

if __name__ == '__main__':
    api = api()
    tweet(api, mensagem.bot_message()) #chama a função que faz tweet no main!
"""

#MÉTODO NOVO (16/11/2023)
if __name__ == '__main__':
    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    client.create_tweet(text = mensagem.bot_message())