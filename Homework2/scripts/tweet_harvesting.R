library("rtweet")

# search tweets using the #harvey
harvey_tweets <- search_tweets("#harvey", n = 100000, retryonratelimit = TRUE, include_rts = FALSE )
save_as_csv(harvey_tweets, "./Dataset/harvey_tweets")
