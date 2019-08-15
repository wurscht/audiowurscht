from django.shortcuts import render
from django.shortcuts import redirect
from webapp.models import Song
from datetime import datetime
import vlc
import mutagen


def MenuView(request):
    return render(request, "index.html")


def UploadView(request):
    if request.method == "POST":
        song_info = mutagen.File(request.FILES["mysong"])
        song = Song(
            title="".join(song_info["TIT2"].text),
            artist="".join(song_info["TPE1"].text),
            album="".join(song_info["TALB"].text),
            path=request.FILES["mysong"],
            tracknumber="".join(song_info["TRCK"].text)
        )
        song.save()
        return redirect("upload")

    return render(request, "song_upload.html")


def PlayView(request):
    songs = Song.objects.all()

    if request.POST.get("play"):
        song_id = request.POST.get("play")
        song = Song.objects.get(id=song_id)
        global player
        player = vlc.MediaPlayer(song.song.path)
        player.play()
    if request.POST.get("stop"):
        player.stop()
    if request.POST.get("pause"):
        player.pause()

    return render(request, "play.html", {"songs": songs})
