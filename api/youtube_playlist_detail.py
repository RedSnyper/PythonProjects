import os
from googleapiclient.discovery import build
import re
from datetime import timedelta


API_KEY = os.environ.get('YOUTUBE_API')
youtube = build('youtube', 'v3', developerKey=API_KEY)

dumpDataFile ='Netflix.txt'                 # filename corresponding to the youtube channel name. Subject to be automatically created later.
channelID ='UCWOA1ZGywLbqmigxE4Qlvuw'       #change only this. Everything else remains the same for all channels on youtube. Subject to be given as input later


requests = youtube.channels().list(
    part='contentDetails',
    id=channelID
)
response = requests.execute()


uploadID = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

youtube_data = []
nextPageToken = None

#################### get all video details of the channel#######################
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=uploadID,
        maxResults=50,
        pageToken=nextPageToken
    )
    pl_response = pl_request.execute()

    vid_ids = []
    for videos in pl_response['items']:
        vid_ids.append(videos['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part='statistics, contentDetails, snippet',
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    for values in vid_response['items']:
        details = {
            'title': values['snippet']['title'],
            'id': values['id'],
            'duration': values['contentDetails']['duration'],
            'view': values['statistics']['viewCount'],
            'like': values['statistics']['likeCount'] if 'likeCount' in values['statistics'] else 0,
            'dislike': values['statistics']['dislikeCount'] if 'dislikeCount' in values['statistics'] else 0,
            'commentCount':values['statistics']['commentCount'] if 'commentCount' in values['statistics'] else 0
        }
        youtube_data.append(details)
    nextPageToken = pl_response.get('nextPageToken')
    if not nextPageToken:
        break

##############################################################################################

###################### use above info to write the result in #################################


hours_pattern = re.compile(r'(\d+)H')
mins_pattern = re.compile(r'(\d+)M')
second_pattern = re.compile(r'(\d+)S')
total_seconds = 0


def secsToTime(time):
    mins, secs = divmod(time, 60)
    hours, mins = divmod(mins, 60)

    return f'{hours} Hours {mins} Minutes {secs} Seconds'


def timeinSeconds(duration):
    hours = hours_pattern.search(duration)
    mins = mins_pattern.search(duration)
    sec = second_pattern.search(duration)
    hours = int(hours.group(1)) if hours else 0
    mins = int(mins.group(1)) if mins else 0
    sec = int(sec.group(1)) if sec else 0
    video_secs = timedelta(hours=hours, minutes=mins, seconds=sec).total_seconds()
    return int(video_secs)


def totalTime(data):
    global total_seconds
    total_seconds += timeinSeconds(data['duration'])
    return total_seconds


def sort(alist):
    return sorted(alist.items(), key=lambda x: x[1], reverse=True)



totalVideoTime = 0
video_time_list = {}
like_list = {}
dislike_list = {}
view_list = {}
comment_list = {}
totalVideos = len(youtube_data)
for item in youtube_data:
    video_time_list[item['title']] = timeinSeconds(item['duration'])
    totalTime(item)
    like_list[item['title']] = int(item['like'])
    dislike_list[item['title']] = int(item['dislike'])
    view_list[item['title']] = int(item['view'])
    comment_list[item['title']] = int(item['commentCount'])

video_time_list = sort(video_time_list)
like_list = sort(like_list)
dislike_list = sort(dislike_list)
view_list = sort(view_list)
comment_list = sort(comment_list)

with open(dumpDataFile, 'w', encoding='UTF-8') as f:
    f.write(f'Total video(s) : {totalVideos}\n')
    f.write(f'Total video time :  {secsToTime(total_seconds)}\n')
    f.write('---------------------------------------------------------------\n')
    f.write(f'Most viewed video : {view_list[0][0]} \n')
    f.write(f'Views : {view_list[0][1]} views\n')
    f.write(f'Least viewed video : {view_list[-1][0]} \n')
    f.write(f'Views : {view_list[-1][1]} views\n')
    f.write('---------------------------------------------------------------\n')
    f.write(f'Longest video : {video_time_list[0][0]}\n')
    f.write(f'Duration : {secsToTime(video_time_list[0][1])}\n')
    f.write(f'Shortest video : {video_time_list[-1][0]}\n')
    f.write(f'Duration : {secsToTime(video_time_list[-1][1])}\n')
    f.write('--------------------------------------------------------------\n')
    f.write(f'Most liked video : {like_list[0][0]} \n')
    f.write(f'Like(s) : {like_list[0][1]} likes\n')
    f.write(f'Least liked video : {like_list[-1][0]} \n')
    f.write(f'Like(s) : {like_list[-1][1]} likes\n')
    f.write('---------------------------------------------------------------\n')
    f.write(f'Most disliked video : {dislike_list[0][0]} \n')
    f.write(f'Dislike(s) :  {dislike_list[0][1]} dislikes\n')
    f.write(f'Least disliked video : {dislike_list[-1][0]} \n')
    f.write(f'Dislike(s) :  {dislike_list[-1][1]} dislikes\n')
    f.write('---------------------------------------------------------------\n')

    f.write(f'Most commented video : {comment_list[0][0]} \n')
    f.write(f'Comment(s) : {comment_list[0][1]} comments\n')
    f.write(f'Least commented video : {comment_list[-1][0]} \n')
    f.write(f'Comment(s) : {comment_list[-1][1]} comments\n')
