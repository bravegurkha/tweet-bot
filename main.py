import tweepy,datetime,requests,json

def tweet():
    consumer_key = "<consumer_key>"
    consumer_secret = "<consumer_secret>"
    access_token = "<access_token>"
    access_token_secret = "<access_token_secret>"
    quote_api_url = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous" #you can use movies instead of famous. See in description.

    quoteData  = requests.get(quote_api_url,headers={
        "X-Mashape-Key": "<X-Mashape-Key>",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      }).json()
    quoteJson = json.loads(json.dumps(quoteData))
    quote = quoteJson['quote']
    tweet = quote + ' #Tweetbot'
    print (tweet)
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)
    api.update_status(tweet)

while (1):
    current_time = datetime.datetime.today()

    if(current_time.hour == 12 and current_time.second == 12):
        tweet()
        print("Tweeted")
