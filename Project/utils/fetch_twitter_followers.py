import tweepy
import time
import csv
import os



directoryPath = os.getcwd()

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

screenNames = ["SenSanders", "CoryBooker", "SenWarren", "marcorubio", "SenJohnMcCain", "RandPaul", "SenTedCruz",
                "SenSchumer", "KamalaHarris", "timkaine"]

#screenNames = ["OSPyoutube"]

ids = []

#print (tweepy.Cursor(api.followers_ids, screen_name="timkaine").items)

for senator in screenNames:
    i = 0
    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=senator).pages():
        print("Currently on page " + str(i) + " for senator" + senator)
        if i == 100: # Gather 500,000 followers for each person
            break
        stringPage = [str(x) for x in page]
        ids.extend(stringPage)
        time.sleep(70)
        i = i + 1


    with open(directoryPath + "/" + senator + 'followers.csv', 'wb') as f:
        writer = csv.writer(f)
        for val in ids:
            writer.writerow([val])


    # resultFile = open(directoryPath + "/" + senator + 'followers.csv','wb')
    # wr = csv.writer(resultFile, delimiter=",")
    # wr.writerows([ids])