from pytubefix import YouTube

def Download(link):
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution();
    youtube_video.download()
    print("Baixou o vídeo.")


link = input("Insira o link do vídeo que deseja baixar: ")
Download(link)