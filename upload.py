import requests

# Replace with your actual access token
access_token = 'EAAVYQWWNQZBoBO0JWlkj4ZAdtgBCfUHgzbc2cpwF0WQ9Blp94cDQZBt45qcnj7J2cW2KWp9eZCMdIrnWkCmYFxjhZBWTykBdB9iuwForqHTfN12M7E6iULi9j9VRoLRDQWEmtquoovVTbE4bZBuZADpDIZAAkIIN6oo6wTNZAa2IHg1q8bALldkmczAFbn0CQXbfr1penmfqZCIMWaOIVaZAekeeo4bpf8XbFSjgRZCUecFeOXpQEvF0nXlr5o08RrBREWYZBZAZB4YqEkZD'


# Video details
video_path = './output/7216822813028584710.mp4'
video_title = 'My Awesome Video'
video_description = 'Check out this amazing video!'

# Upload video
upload_url = f'https://graph-video.facebook.com/v12.0/me/videos?access_token={access_token}'
files = {
    'source': (video_path, open(video_path, 'rb')),
    'title': (None, video_title),
    'description': (None, video_description)
}

video_upload_response = requests.post(upload_url, files=files)

try:
    video_id = video_upload_response.json()['video_id']
    print(f'Video uploaded with ID: {video_id}')
except KeyError:
    print('Failed to upload video:', video_upload_response.text)

# Post video details
post_url = f'https://graph.facebook.com/v12.0/me/feed?access_token={access_token}'
post_data = {
    'message': video_description,
    'attached_media': [
        {
            'media_fbid': video_id
        }
    ]
}

post_response = requests.post(post_url, json=post_data)

if post_response.status_code == 200:
    print('Video posted successfully!')
else:
    print('Failed to post video:', post_response.json())
