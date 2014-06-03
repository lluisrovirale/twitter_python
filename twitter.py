from twython import *

TWITTER_APP_KEY = 'HERE DE KEY' #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'HERE THE KEY' 
TWITTER_ACCESS_TOKEN = 'HERE THE KEY'
TWITTER_ACCESS_TOKEN_SECRET = 'HERE THE KEY'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#etsetb',   #**supply whatever query you want here**
                  count=1000)

tweets = search['statuses']

#for tweet in tweets:
  #print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
print len(tweets)