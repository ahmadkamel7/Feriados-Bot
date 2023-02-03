import tweepy
import keys
import mensagem


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