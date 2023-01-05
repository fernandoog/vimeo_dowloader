from vimeo_downloader import Vimeo

# Replace these with other list of videos you want to download
videos = ['https://vimeo.com/766411266']

for video in videos:
    v = Vimeo(video)
    stream = v.streams  # List of available streams of different quality

    # Selecting and downloading '720p' video
    for s in stream:
            s.download(download_directory='video', filename=v.metadata.title)
    else:  # If the loop never break
        print('quality not found')