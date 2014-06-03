from twython import Twython, TwythonError
i=1
# Requires Authentication as of Twitter API v1.1
APP_KEY = 'HERE DE KEY' #supply the appropriate value
APP_SECRET = 'HERE THE KEY' 
OAUTH_TOKEN = 'HERE THE KEY'
OAUTH_TOKEN_SECRET = 'HERE THE KEY'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

hashtag='#dilluns'


try:
    search_results = twitter.search(q=hashtag,count=100)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n' 'Compta en:', i,'\n'
    i=i+1

print 'He trobat: ',len(search_results['statuses']), 'tweets amb el hastag', hashtag