import tweepy

ckey = '***************'
csecret = '*********'
access_token = '***********'
access_secret_token = '************'

authorization = tweepy.OAuthHandler(ckey,csecret)
authorization.set_access_token(access_token,access_secret_token)
api = tweepy.API(authorization)

api.update_status('This is  my second test tweet')




