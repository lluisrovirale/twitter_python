from twython import TwythonStreamer

APP_KEY = 'HERE DE KEY' #supply the appropriate value
APP_SECRET = 'HERE THE KEY' 
OAUTH_TOKEN = 'HERE THE KEY'
OAUTH_TOKEN_SECRET = 'HERE THE KEY'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data

# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='#elecciones',language='es')
#stream.user()  # Read the authenticated users home timeline (what they see on Twitter) in real-time
#stream.site(follow='twitter')