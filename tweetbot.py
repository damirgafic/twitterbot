import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
# print(user.name)
print(user.screen_name)
print(user.followers_count)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)  # 1000 ms or 1 second
    except StopIteration:
        print('Successfully traversed through followers list!')


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_status(self, status):
        print(status.text)
        '''self.num_tweets += 1
        if self.num_tweets < 5:
            return True
        else:
            return False'''


stream = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream)
limit_handle(stream.filter(follow=["4185334874"]))


'''
search_string = 'Damir'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
'''

'''
# Generous_bot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
   # if follower.name == 'yugomemes':
    #    follower.follow()
    print(follower.name)
'''
