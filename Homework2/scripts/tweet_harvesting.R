#setwd("~/Desktop/Data Analytics/HW")
setwd("~/Google Drive/TTU/2017 Fall/Data Analytics/HW/")
library("rtweet")

# search tweets using the #harvey
harvey_tweets <- search_tweets("#harvey", n = 10, lang="en", retryonratelimit = TRUE, include_rts = FALSE )
# save_as_csv(harvey_tweets, "harvey_tweets")

harvey_tweets


# library(twitteR)
# 
# consumer_key <- '9OSed6UiQsQGturD6bF5TqvWF'
# consumer_secret <- '6LAQKFVWTC8J0f5IJ1cvZw9y2L4hP95lrHqXIkpcLXL2jjT23b'
# access_token <- '78524195-7o8FbLYkgBHqoR5lrEVdEmIKPKbzF4SGFsTG1RRKU'
# access_secret <- 'vfZ40u9N0ksEJguddAIlPXOB1WGy6j5gpzm7grlBxF5oe'
# setup_twitter_oauth(consumer_key, consumer_secret, access_token, access_secret)
# 
# #crawling twitter
# harvey <- searchTwitter("#harvey", n=500, lang="en", since='2017-08-26')
# 
