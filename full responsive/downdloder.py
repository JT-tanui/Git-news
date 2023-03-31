from pytube import YouTube

def Downdload(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.downdload()
    except:
        print("There is an error in downloading the video")
    print("The download has completed! Awesome.")



    
