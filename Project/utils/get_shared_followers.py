import csv
import os

os.chdir('..')

directoryPath = os.getcwd()+ '\SenatorDataSets'

def get_shared_followers():
    # Grab the follower csvs from the datasets folder
    csvPaths = [directoryPath + '/' + p for  p in os.listdir(directoryPath) if 'followers' in p]

    for i in range(0, len(csvPaths)):
        f1 = file(csvPaths[i], 'r')
        csv1 = csv.reader(f1)
        L1 = [item for sublist in [x for x in csv1] for item in sublist]
        for j in range(1, len(csvPaths)):

            f2 = file(csvPaths[j], 'r')
            csv2 = csv.reader(f2)
            L2 = [item for sublist in [x for x in csv2] for item in sublist]

            f3Path = directoryPath + '/' + os.path.basename(csvPaths[i]).replace("followers.csv", "") + '_' + os.path.basename(csvPaths[j]).replace("followers.csv", "") + '_' +'SharedFollowers.csv'

            # hold shared follower ids
            f3 = file(f3Path, 'w')
            csv3 = csv.writer(f3)
            L3 = list(set(L1).intersection(L2))

            with open(f3Path, 'wb') as f:
                writer = csv.writer(f)
                for val in L3:
                    writer.writerow([val])

            print 'Finished writing shared followers for ' + os.path.basename(csvPaths[i]) + ' and ' + os.path.basename(csvPaths[j])

def get_shared_followers(folderPath):

    csvPaths = [folderPath + '/' + p for p in os.listdir(folderPath)]
    L = [['Senators', 'Percent Shared Followers']]

    for data in csvPaths:
        fileObject = file(data)
        row_count = sum(1 for row in fileObject)

        basename = (os.path.basename(data)).split('_')

        item = ['@' + basename[0] + ' and ' + '@' + basename[1] + ' Shared Followers', row_count/float(500000)]


        L.append(item)

    print(L)

    with open(folderPath + '/' + 'SharedFollowerRatios.csv', "wb") as f:
        writer = csv.writer(f)
        writer.writerows(L)

sharedDirectory = directoryPath + '/SharedFollowers'
get_shared_followers(sharedDirectory + '/DtoR')
get_shared_followers(sharedDirectory + '/RtoR')