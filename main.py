import tweepy
import keys
import mensagem

#MÉTODO NOVO (16/11/2023)
if __name__ == '__main__':
    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    client.create_tweet(text = mensagem.bot_message())