from pytube import YouTube
import os
os.system("pip install git+https://github.com/Zeecka/pytube@fix_1060")

print("--------------------url----------------")
k=input("what is your url of the video::")
if "https"or "http" in k :
    try:
        print(k)
        video=YouTube(k)
        print("########################TITLE##############")
        print(video.title)
        print("_________________________thumbnail image___________________")
        print(video.thumbnail_url)
        print("______________________Download video_________________________________")
        print("!!!!!!!!!!!!!!!!!Download!!!!!!!!!!!!!!!!!!")
        #for stream in video.streams:
            #print(stream)
        video=video.streams.get_highest_resolution()
        video.download()
        print("sucess")
    except Exception as e:
        print("somthing is going wrong the webpage may be removed or under maintanence")
        print(e)
else:
    print("invalid address!")
