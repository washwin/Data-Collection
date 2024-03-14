import csv
import time
import twikit

USERNAME = 'DataC51466'
EMAIL = '210010060@iitdh.ac.in'
PASSWORD = 'KSijNdwXdJJd799'
# Initialize client
client = twikit.Client('en-US')
# Login to the service with provided user credentials
client.login(
    auth_info_1=USERNAME ,
    auth_info_2=EMAIL,
    password=PASSWORD
)
print("Authentication successful")
hash_tags = "#KukiMilitant #SaveManipur #Savemeiteis #Ethniccleansing #kukimilitants #kuki #meitei #visitManipur #Kuki_ZoEngineeredViolence #SaveMoreh #SaveManipurSaveIndia #MorehBurning #ManipurFights Back #KukiMilitantvioleteSoO #AbrogateSoO #poppy #illegalImmigration #terror #Sanamahi #7MonthsOfNoInternet #StopTheViolence #MyManipur #Stand4Manipur #ManipurUnderAttack #StopGenocideofMeiteis #lies #genocide #KukiLiesXposed #KukiAtrocites #KukiZoEngineerdManipurConflict #meiteiyouths #KukiWarCrimes #PoppyCultivators #kukinarcoterrorist #Narcokukiterrorist #SavekukiZoTribals #ManipurCrisis #KukiRapist #AssamRifles#lamkatalk #stoppoppycultivators #kukizo #kukizolivesmatter #ManipurPolice #FailedGovernment #manipurisburning #MeiteiMilitant "
hashtags = hash_tags.split()

NEXTPAGE = 1

with open('manipur_violence.csv', 'w', newline='') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)
    # csv_writer.writerow(['hashtag', 'text', 'favorite_count'])    
    csv_writer.writerow(['id', 'text', 'favorite_count', 'created_at', 'author', 'language', 'retweet_count', 'media', 'view_count', 'replies'])
    for hashtag in hashtags:
        print(f"Finding tweets on {hashtag}")
        while True:
            try:
                tweets = client.search_tweet(hashtag, 'Latest')
                for tweet in tweets:
                    tweet = client.get_tweet_by_id(tweet.id)
                    # csv_writer.writerow([hashtag, tweet.text, tweet.favorite_count])
                    csv_writer.writerow([tweet.id, tweet.text, tweet.favorite_count, tweet.created_at, tweet.user.name, tweet.lang, tweet.retweet_count, tweet.media, tweet.view_count, tweet.replies])
                    
                # for i in range(NEXTPAGE):
                #     more_tweets = client.search_tweet(hashtag, 'Latest')
                #     for tweet in more_tweets:
                #         tweet = client.get_tweet_by_id(tweet.id)
                #         csv_writer.writerow([hashtag, tweet.text, tweet.favorite_count])
                        # csv_writer.writerow([tweet.id, tweet.text, tweet.favorite_count, tweet.created_at, tweet.user.name, tweet.lang, tweet.retweet_count, tweet.media, tweet.view_count, tweet.replies])
                
                break
            except twikit.errors.TooManyRequests:
                print("Rate limit exceeded. Waiting for 15 minutes...")
                time.sleep(1000)
            except Exception as e:
                print("An error occurred:", e)
                continue