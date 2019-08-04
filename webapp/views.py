from django.shortcuts import render
from django.shortcuts import redirect
from webapp.models import Song
import vlc


def IndexView(request):
    if request.method == 'POST':
        song = Song(
            name=str(request.FILES['mysong']),
            song=request.FILES['mysong']
        )
        song.save()
        return redirect('/')

    return render(request, 'song_upload.html')


def PlayView(request):
    songs = Song.objects.all()

    if request.POST.get('play'):
        song_id = request.POST.get('play')
        song = Song.objects.get(id=song_id)
        global player
        player = vlc.MediaPlayer(song.song.path)
        player.play()
    if request.POST.get('stop'):
        player.stop()

    return render(request, 'play.html', {
        'songs': songs
    })
