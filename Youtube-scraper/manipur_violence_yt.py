# %%
from googleapiclient.discovery import build
import pandas as pd

# %%
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyD_s3lu76rpoAt_Ym6WC87-KFFBTxPj3hY"
youtube = build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

# %%
def get_comments_in_videos(youtube, video_ids):
    all_comments = []
    
    for video_id in video_ids:
        try:   
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id
            )
            response = request.execute()
        
            comments_in_video = [comment['snippet']['topLevelComment']['snippet']['textOriginal'] for comment in response['items'][0:10]]
            comments_in_video_info = {'video_id': video_id, 'comments': comments_in_video}

            all_comments.append(comments_in_video_info)
            
        except: 
            # When error occurs - most likely because comments are disabled on a video
            print('Could not get comments for video ' + video_id)
        
    return pd.DataFrame(all_comments) 

# %%
video_ids = ['cj1_lJULOuY', 'WH7Sk9KOD84', 'Qg0W5cmFcmU', 'kBQ-MAtaxEc', 'a9dEwHVYjEM', 'xJjgUbvSAJs']

# %%
comments = get_comments_in_videos(youtube, video_ids)

# %%
comments.to_csv("manipur_violence_youtube.csv")


