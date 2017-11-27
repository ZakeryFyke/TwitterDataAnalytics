import csv
import os


os.chdir('..')

directoryPath = os.getcwd()+ '\SenatorDataSets'

def get_followers_of_all_party_members(party):
    subDirectoryPath = directoryPath + '/' + party

    # Grab all the follower csvs for this party
    csvPaths = [subDirectoryPath + '/' + p for p in os.listdir(subDirectoryPath) if 'followers' in p]

    f1 = file(csvPaths[0], 'r')
    csv1 = csv.reader(f1)
    L1 = [item for sublist in [x for x in csv1] for item in sublist]

    for i in range(1, len(csvPaths)):
        f2 = file(csvPaths[i], 'r')
        csv2 = csv.reader(f2)
        L2 = [item for sublist in [x for x in csv2] for item in sublist]

        # Get common items between L1 and L2
        L1 = list(set(L1).intersection(L2))

    sharedPath = subDirectoryPath + '/' + 'FollowersOfAll' + party + '.csv'

    with open(sharedPath, 'wb') as f:
        writer = csv.writer(f)
        for val in L1:
            writer.writerow([val])


def merge_party_followers(party):
    subDirectoryPath = directoryPath + '/' + party

    # Grab all the follower csvs for this party
    csvPaths = [subDirectoryPath + '/' + p for p in os.listdir(subDirectoryPath) if 'followers' in p]

    print("Adding up a total of " + str(len(csvPaths)) + "csvs")
    f1 = file(csvPaths[0], 'r')
    csv1 = csv.reader(f1)
    L1 = [item for sublist in [x for x in csv1] for item in sublist]

    for i in range(1, len(csvPaths)):
        f2 = file(csvPaths[i], 'r')
        csv2 = csv.reader(f2)
        L2 = [item for sublist in [x for x in csv2] for item in sublist]

        # Get items in L2 that aren't in L1
        L1 = L1 + list(set(L2).difference(L1))

        sharedPath = subDirectoryPath + '/' + 'All' + party + 'Followers.csv'

        with open(sharedPath, 'wb') as f:
            writer = csv.writer(f)
            for val in L1:
                writer.writerow([val])

    print("Finished " + party + " with final count of " + str(len(L1)) + " followers")


# Merge the tweet files for each party

def merge_party_tweets(party):
    subDirectoryPath = directoryPath + '/' + party

    # Grab all the follower csvs for this party
    csvPaths = [subDirectoryPath + '/' + p for p in os.listdir(subDirectoryPath) if 'tweets' in p]

    print("Adding up a total of " + str(len(csvPaths)) + "csvs")
    f1 = file(csvPaths[0], 'r')
    csv1 = csv.reader(f1)
    L1 = [item for sublist in [x for x in csv1] for item in sublist]

    for i in range(1, len(csvPaths)):
        f2 = file(csvPaths[i], 'r')
        csv2 = csv.reader(f2)
        L2 = [item for sublist in [x for x in csv2] for item in sublist]

        # Get items in L2 that aren't in L1
        L1 = L1 + list(set(L2).difference(L1))

        sharedPath = subDirectoryPath + '/' + 'All' + party + 'Tweets.csv'

        with open(sharedPath, 'wb') as f:
            writer = csv.writer(f)
            for val in L1:
                writer.writerow([val])

    print("Finished " + party + " with final count of " + str(len(L1)) + " tweets")

# Find followers of all one party, and none of the other party.
# This entire thing should probably be parameterized, but meh.
def find_exclusive_all_followers():
    repPath = directoryPath + '/' + 'Republicans' + '/' + 'ExclusiveRepublicans.csv'
    demPath = directoryPath + '/' + 'Democrats' + '/' + 'ExclusiveDemocrats.csv'

    reps = file(repPath, 'r')
    repCsv = csv.reader(reps)
    repList = [item for sublist in [x for x in repCsv] for item in sublist]

    dems = file(demPath, 'r')
    demCsv = csv.reader(dems)
    demList = [item for sublist in [x for x in demCsv] for item in sublist]

    exclusiveReps = list(set(repList).difference(demList))
    exclusiveDems = list(set(demList).difference(repList))

    exclusiveRepPath = directoryPath + '/' + 'Republicans' + '/' + 'ExclusiveRepublicans.csv'
    exclusiveDemPath = directoryPath + '/' + 'Democrats' + '/' + 'ExclusiveDemocrats.csv'

    with open(exclusiveRepPath, 'wb') as f:
        writer = csv.writer(f)
        for val in exclusiveReps:
            writer.writerow([val])

    with open(exclusiveDemPath, 'wb') as f:
        writer = csv.writer(f)
        for val in exclusiveDems:
            writer.writerow([val])

# Gets all followers into a single csv
def get_all_followers():

    print(directoryPath + '/Republicans/')

    csvPaths = [directoryPath + '/Republicans/' + p for p in os.listdir(directoryPath + '/Republicans') if 'followers' in p] + \
               [directoryPath + '/Democrats/' + p for p in os.listdir(directoryPath + '/Democrats') if 'followers' in p]

    if(len(csvPaths) > 0):
        f1 = file(csvPaths[0], 'r')
        csv1 = csv.reader(f1)
        L1 = [item for sublist in [x for x in csv1] for item in sublist]

        for i in range(1, len(csvPaths)):
            f2 = file(csvPaths[i], 'r')
            csv2 = csv.reader(f2)
            L2 = [item for sublist in [x for x in csv2] for item in sublist]

            # Add items in L2 which aren't in L1
            L1 = L1 + list(set(L2).difference(L1))

        finalPath = directoryPath + '/' + 'AllFollowers.csv'

        with open(finalPath, 'wb') as f:
            writer = csv.writer(f)
            for val in L1:
                writer.writerow([val])
    else:
        print("Nothing to do.")

    print("Finished. Total length: " + str(len(L1)))

# Followers of at least one of this party and none of the other
def get_exclusive_followers():
    repPath = directoryPath + '/' + 'Republicans' + '/' + 'All' + 'Republicans' + 'Followers.csv'
    demPath = directoryPath + '/' + 'Democrats' + '/' + 'All' + 'Democrats' + 'Followers.csv'

    reps = file(repPath, 'r')
    repCsv = csv.reader(reps)
    repList = [item for sublist in [x for x in repCsv] for item in sublist]

    dems = file(demPath, 'r')
    demCsv = csv.reader(dems)
    demList = [item for sublist in [x for x in demCsv] for item in sublist]

    # Those in the Republican csv not in the Democrat csv
    exclusiveReps = list(set(repList).difference(demList))

    # Those in the Democrat csv not in the Republican csv
    exclusiveDems = list(set(demList).difference(repList))

    exclusiveRepPath = directoryPath + '/' + 'ExclusiveRepublicans_Any.csv'
    exclusiveDemPath = directoryPath + '/' + 'ExclusiveDemocrats_Any.csv'

    print('Republicans: ' + str(len(exclusiveReps)))
    print('Democrats: ' + str(len(exclusiveDems)))

    with open(exclusiveRepPath, 'wb') as f:
        writer = csv.writer(f)
        for val in exclusiveReps:
            writer.writerow([val])

    with open(exclusiveDemPath, 'wb') as f:
        writer = csv.writer(f)
        for val in exclusiveDems:
            writer.writerow([val])


parties = ['Republicans', 'Democrats']

# for party in parties:
#     merge_party_tweets(party)

get_exclusive_followers()
