from django.shortcuts import render
# from webapp.forms import SongForm
from django.shortcuts import redirect
from webapp.models import Song


def index(request):
    songs = Song.objects.all()
    if request.method == 'POST':
        song = Song(
            name=str(request.FILES['mysong']),
            song=request.FILES['mysong']
        )
        song.save()
        return redirect('/')

    return render(request, 'song_upload.html', {
        'songs': songs
    })
