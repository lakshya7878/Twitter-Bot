import tweepy

ckey = 'ojnv1gy3V9azhBcAVCqEskZ55'
csecret = 'NKTDcGoeAYp2Lpp8xQKi4WJIGAwK0WjxNQtWVh009asVMktroH'
access_token = '1440308563537104905-5IegzSAYBEdEEAY7cvX8CK0RxmZiC4'
access_secret_token = '0itPfBAWF5x601HOEFmvNP4vsdZNTUvyY3rmK1NpqULit'

authorization = tweepy.OAuthHandler(ckey,csecret)
authorization.set_access_token(access_token,access_secret_token)
api = tweepy.API(authorization)

api.update_status('This is  my second test tweet')




