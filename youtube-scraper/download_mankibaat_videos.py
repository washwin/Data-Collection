import pandas as pd
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("Starting download")
        youtubeObject.download('./downloads')
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def check_age_restriction(link,vid):
    youtubeObject = YouTube(link)
    if youtubeObject.age_restricted:
        print(vid)
    else:
        print("*")
def main():
    channel_id = "SansadTV"
    playlist_id = "PLVOgwA_DiGzotAXVMDT50J2fp9w8ASRC7"
    vid_df = pd.read_csv("mankibaat_video_ids.csv")
    for ind in vid_df.index:
        link = "https://www.youtube.com/watch?v={}&list={}&ab_channel={}".format(vid_df.loc[ind,"video_ids"],playlist_id,channel_id)
        # print(link)
        # Download(link)
        vid = vid_df.loc[ind,"video_ids"]
        check_age_restriction(link, vid)


main()