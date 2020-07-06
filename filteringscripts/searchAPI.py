#!/usr/bin/env python
import tweepy

f = open('credentials.txt', 'r')
lines = f.read().splitlines()

consumer_key = lines[0]
consumer_key_secret = lines[1]
access_token = lines[2]
access_token_secret = lines[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = list()
keywords = []
with open('keywords/groningen', 'r') as keywordsfile:
    for line in keywordsfile:
        keywords.append(line)
#with open('groningenfiltered', 'r') as keywords:
    #with open('corpus', 'w+') as corpus:
        #for keyword in keywords:
            #search_results = api.search(q=keyword + " geocode:53.291224,6.630148,24", count=1, tweet_mode='extended')
            #for tweet in search_results:
                #corpus.write(tweet.full_text)
                #corpus.write('\n')
print(api.rate_limit_status())
with open('corpus', 'w+') as corpus:
    for keyword in keywords:
        print(keyword)
        search_results = api.search(q= keyword + " geocode:53.291224,6.630148,24", count=1000, tweet_mode='extended')

        for tweet in search_results:
            corpus.write("{}\t{}".format(keyword, tweet.full_text))
            corpus.write('\n')



