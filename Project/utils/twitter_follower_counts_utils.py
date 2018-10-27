import tweepy
import time
import json
from pprint import pprint
import csv
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

consumer_key = 'LCZYEEJeF3MkeFh1JxTxB7wJ7'
consumer_secret = 'RAHCB05ZiEtuYcx39HRZUU4umpaKEyg9ehp6UkID2kkdPuirkZ'
access_token = '716416423-1N95YfJuIRSyu7LtecfTtgAyXahWejYppcL5v110'
access_secret = 'x1tE0tGROEoN4eUZoPlfhJQDZazEXsWwx8GHMlXja8c3q'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# user = api.get_user('ZakeryAlexander')
# print user.screen_name
# print user.followers_count
# screenNames = ["SenSanders", "CoryBooker", "SenWarren", "marcorubio", "SenJohnMcCain", "RandPaul", "SenTedCruz",
#                    "SenSchumer", "KamalaHarris", "timkaine"]
#u'RepConorLamb'
# for senator in screenNames:
#     for user in tweepy.Cursor(api.followers, screen_name=senator).items():
#         print user.screen_name, user.followers_count

def add_party_to_csv():

    # Dataframe of Senators' twitter handle and their follower count
    senator_follower_data = pd.read_csv('rep_followers_with_id.csv', index_col="Unnamed: 0")

    senator_follower_data['party'] = ''

    with open(r"Z:\Research\TwitterDataAnalytics\Datasets\legislators-current.json") as f:
        senator_personal_data = json.load(f)

    for index, row in senator_follower_data.iterrows():

        bioguide = row['id']

        match = [x for x in senator_personal_data if x['id']['bioguide'] == bioguide][-1]

        party = match['terms'][-1]['party']

        senator_follower_data.set_value(index, 'party', party)

    senator_follower_data.to_csv("rep_data_all_cols.csv")


def add_id_to_twitter_follower_csv():
    with open(r"Z:\Research\TwitterDataAnalytics\Datasets\legislators-social-media.json") as f:
        data = json.load(f)

    senator_follower_data = pd.read_csv('dict.csv', names=["name", "followers"])
    senator_follower_data['id'] = ""
    print(senator_follower_data)

    for index, row in senator_follower_data.iterrows():
        handle = row['name']
        match = [x for x in data if('social' in x and 'twitter' in x['social']) and ('id' in x and 'bioguide' in x['id'])
                 and x['social']['twitter'] == handle][-1]['id']['bioguide']

        senator_follower_data.set_value(index, 'id', match)

    print(senator_follower_data)

    senator_follower_data.to_csv("rep_followers_with_id.csv")


def get_twitter_follower_counts():
    with open(r"Z:\Research\TwitterDataAnalytics\Datasets\legislators-social-media.json") as f:
        data = json.load(f)
    count = 0
    senator_dict = dict()

    for senator in data:
        if 'social' in senator:
            if 'twitter' in senator['social']:
                pprint(senator['social']['twitter'])

                user = api.get_user(senator['social']['twitter'])

                senator_dict[senator['social']['twitter']] = user.followers_count

                count += 1

                time.sleep(5)
    print(count)

    # Write to csv
    with open('dict.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in senator_dict.items():
           writer.writerow([key, value])


def visualize_senator_followers():
    data = pd.read_csv("rep_data_all_cols.csv")
    data = data.sort(['followers'], ascending=False)

    data = data
    print(data)

    colors = []

    for index, row in data.iterrows():
        if(row['party'] == 'Democrat'):
            colors.append('b')
        elif(row['party'] == 'Republican'):
            colors.append('r')
        else:
            colors.append('gray')

    data.plot(kind='bar', x='name', y='followers', color=colors, logy=True)

    independents = mpatches.Patch(color='gray', label='Independents')
    democrats = mpatches.Patch(color='blue', label='Democrats')
    republicans = mpatches.Patch(color='red', label='Republicans')

    plt.legend(handles=[independents, democrats, republicans])

    plt.show()

    print(data['followers'].median())


visualize_senator_followers()
















