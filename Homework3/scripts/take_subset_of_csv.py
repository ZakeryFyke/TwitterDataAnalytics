import random
import csv

filePath = './../Dataset/harvey_tweets.tweets.csv';

fileSize = 76836

f = open(filePath,mode='r', encoding="ascii", errors='ignore')

newCsv = set()

helpWords = ['help', 'rescue', 'donate', 'aid', 'relief', 'charity', 'charities', 'donating', 'donors', 'please']
i = 0

normalLines = []
usedLines = []
print("Starting \n")
while (len(newCsv) < 1000):
    offset = random.randrange(fileSize)
    #f.seek(offset)  # go to random position
    f.readline()
    random_line = f.readline()

    # Prevent duplicates
    #if offset in normalLines:
     #   continue

    #if (len(random_line) > 100) & (not random_line in newCsv):
    x = random_line.split(',')
    print(len(x))
    if (len(x) > 35):
        if(len(x[4]) > 30):
            if any(ext in random_line for ext in helpWords):
                new_line = x[4] + ',' + 'Rescue'
                newCsv.add(new_line)
                normalLines.append(offset)
            else:
                new_line = x[4] + ',' + 'Non-Rescue'
                newCsv.add(new_line)
                normalLines.append(offset)


print("Finished initial")
while (len(newCsv) < 1750):
    offset = random.randrange(fileSize)
    #f.seek(offset)  # go to random position
    random_line = f.readline()

    x = random_line.split(',')
    #if (offset in usedLines):
     #   continue
    if (len(x) > 35):
        if (len(x[4]) > 30):
            if any(ext in random_line for ext in helpWords):
                new_line = x[4] + ',' + 'Rescue'
                newCsv.add(new_line)
                usedLines.append(offset)

print("Made it to here")

writer = csv.writer(open('./../Dataset/harvey_tweets.sample.csv', 'w', encoding='utf-8', newline=''))
for item in newCsv:
    l = item.split(',')
    writer.writerow(l)
print("Done")