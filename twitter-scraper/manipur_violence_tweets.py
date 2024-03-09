import csv
import time
import twikit

USERNAME = 'DataC51466'
EMAIL = 'xxxxxxxxxxxxxxx'
PASSWORD = 'xxxxxx'
# Initialize client
client = twikit.Client('en-US')
# Login to the service with provided user credentials
client.login(
    auth_info_1=USERNAME ,
    auth_info_2=EMAIL,
    password=PASSWORD
)

hash_tags = "#KukiMilitant #SaveManipur #Savemeiteis #Ethniccleansing #kukimilitants #kuki #meitei #visitManipur #Kuki_ZoEngineeredViolence #SaveMoreh #SaveManipurSaveIndia #MorehBurning #ManipurFights Back #KukiMilitantvioleteSoO #AbrogateSoO #poppy #illegalImmigration #terror #Sanamahi #7MonthsOfNoInternet #StopTheViolence #MyManipur #Stand4Manipur #ManipurUnderAttack #StopGenocideofMeiteis #lies #genocide #KukiLiesXposed #KukiAtrocites #KukiZoEngineerdManipurConflict #meiteiyouths #KukiWarCrimes #PoppyCultivators #kukinarcoterrorist #Narcokukiterrorist #SavekukiZoTribals #ManipurCrisis #KukiRapist #AssamRifles#lamkatalk #stoppoppycultivators #kukizo #kukizolivesmatter #ManipurPolice #FailedGovernment #manipurisburning #MeiteiMilitant "
hashtags = hash_tags.split()

NEXTPAGE = 1

with open('manipur_violence.csv', 'w', newline='') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)
    csv_writer.writerow(['hashtag', 'text', 'favorite_count'])    
    
    for hashtag in hashtags:
        while True:
            try:
                tweets = client.search_tweet(hashtag, 'Latest')
                for tweet in tweets:
                    tweet = client.get_tweet_by_id(tweet.id)
                    csv_writer.writerow([hashtag, tweet.text, tweet.favorite_count])
                    
                for i in range(NEXTPAGE):
                    more_tweets = client.search_tweet(hashtag, 'Latest')
                    for tweet in more_tweets:
                        tweet = client.get_tweet_by_id(tweet.id)
                        csv_writer.writerow([hashtag, tweet.text, tweet.favorite_count])
                
                break
            except twikit.errors.TooManyRequests:
                print("Rate limit exceeded. Waiting for 15 minutes...")
                time.sleep(15 * 60)
            except Exception as e:
                print("An error occurred:", e)
                continue