from pytube import YouTube ,Playlist

def playlist_video(link):
    try:
        liste = Playlist(link)
        indirilenvideosayisi = 1
        print(f"playlistte {len(liste.video_urls)} adet video bulunmaktadır")
        filename = input("lütfen klasör ismi giriniz : \n")
        for i in liste.videos:
            print(f"{indirilenvideosayisi}-)şuanda indirilen video ismi : {i.title} ")
            i.streams.get_highest_resolution().download(filename)
            indirilenvideosayisi += 1
        print(f"Playlistte bulunan {indirilenvideosayisi} video başarı ile indirildi")
    except:
        print("işlem sırasında bilinmeyen bir sorunla karşılaşıldı.")

def playlist_ses(link):
    try:
        liste = Playlist(link)
        indirilenvideosayisi = 1
        print(f"playlistte {len(liste.video_urls)} adet video bulunmaktadır")
        filename = input("lütfen klasör ismi giriniz : \n")
        print("İndiriliyor")
        for i in liste.videos:
            print(f"{indirilenvideosayisi}-) şuan da inen şarkı : {i.title}")
            video_ismi = i.title.replace("/","").replace('"',"").replace(":","").replace("*","").replace("?","").replace("<","").replace(">","").replace("|","")
            i.streams.get_audio_only().download(filename,video_ismi+".mp3")
            indirilenvideosayisi += 1
        print(f"Playlistte bulunan {indirilenvideosayisi} ses başarı ile indirildi")
    except:
        print("işlem sırasında bilinmeyen bir sorunla karşılaşıldı.")

def sesindirme(link):
    try:
        yt = YouTube(link)
        print(yt.title)
        ys = yt.streams.filter(mime_type="audio/mp4").first()
        print("İndiriliyor")
        video_ismi = ys.title.replace("/","").replace('"',"").replace(":","").replace("*","").replace("?","").replace("<","").replace(">","").replace("|","")
        ys.download("ses",video_ismi+".mp3")
        print("dosya başarıyla indirildi.")
    except:
        print("işlem sırasında bilinmeyen bir sorunla karşılaşıldı.")

def videoindirme(link):
    try:
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        print(ys.title)
        print("İndiriliyor")
        ys.download("video")
        print("Başarıyla indirildi")
    except:
        print("işlem sırasında bilinmeyen bir sorunla karşılaşıldı.")


değer = True
while değer :
    secenek = input("1-)mp3 indir\n2-)mp4 indir\n3-)mp3 PLayList indir\n4-)mp4 Playlist indir\n5-)çıkış yap(exit)\nişlem numrasını veya çıkmak için exit yazın ve enter tuşuna basın.\n")
    if(secenek == "1"):
        link = input("link  :")
        sesindirme(link)

    elif(secenek == "2"):
        link = input("link  :")
        videoindirme(link)

    elif secenek == "3":
        link = input("link  :")
        playlist_ses(link)

    elif secenek == "4":
        link = input("link  :")
        playlist_video(link)
    elif secenek == "exit" or secenek == "5":
        değer = False
        print("çıkış yapılıyor...")
    else:
        print("lütfen geçerli bir seçenek giriniz.")