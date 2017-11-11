import tweepy
import re
import csv
import os

consumer_key=''
consumer_secret=''
access_token=''
access_secret=''

directoryPath = os.getcwd()

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

screenNames = ["SenSanders", "CoryBooker", "SenWarren", "marcorubio", "SenJohnMcCain", "RandPaul", "SenTedCruz",
                 "SenSchumer", "KamalaHarris", "timkaine"]

# # The ids for all senators above, in order.
# twitterIDs = ["29442313", "15808765", "970207298", "15745368", "19394188", "216881337", "1074480192",
#               "17494010", "30354991", "172858784"]

# holds tweets for the senator
alltweets = []

# below heavily pulled from https://gist.github.com/yanofsky/5436496
for senator in screenNames:
    alltweets = []

    new_tweets = api.user_timeline(screen_name = senator, count = 200, tweet_mode="extended")

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id -1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=senator, count=200, max_id=oldest, tweet_mode="extended")

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[re.sub(r"http\S+", "",tweet.full_text.replace(',', '').replace('\n','').replace("RT ", "")).encode("utf-8")] for tweet in alltweets]

    with open(directoryPath + "/" + senator + 'tweets.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)


