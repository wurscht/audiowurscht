import os
import base64
import vlc
import mutagen
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from webapp.models import Song, Profile
from webapp.forms import RegistrationForm
from django.views import generic


def MenuView(request):
    current_user = request.user
    return render(request, "index.html", {
        "user": current_user
    })


class RegistrationView(FormView):
    model = User
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = '/send_confirmation_mail'

    def form_valid(self, form):
        user = User.objects.create_user(form.data['username'],
                                        form.data['email'],
                                        form.data['password1'],
                                        first_name=form.data['first_name'],
                                        last_name=form.data['last_name'])
        user.is_active = False
        user.save()

        if user is not None:
            self.generate_profile(user)

        return super(RegistrationView, self).form_valid(form)

    def generate_key(self):
        return base64.b32encode(os.urandom(7))[:10].lower()

    def generate_profile(self, user):
        profile = Profile(key=self.generate_key(), user=user)
        profile.save()
        send_mail(
            'Mate Counter account confirmation',
            """
            Hello,
            please click this link to activate your Mate Counter account:
            {0}/registration_done/{1}
            Sincerely,
            The Mate Counter Team
            """.format(settings.SITE_URL, profile.key.decode("utf-8")),
            'info@audiowurscht.com',
            [user.email],
            fail_silently=False,
        )


class RegistrationDoneView(generic.TemplateView):
    template_name = 'registration/registration_done.html'

    def get_context_data(request, key):
        matches = Profile.objects.filter(key=key.encode("utf-8"))
        if matches.exists():
            profile = matches.first()
            if profile.user.is_active:
                request.template_name = (
                    'registration/user_is_already_active.html')
            else:
                profile.user.is_active = True
                profile.user.save()
        else:
            request.template_name = 'registration/registration_failed.html'


def send_confirmation_mail_view(request):
    return render(request, "registration/send_confirmation_mail.html")


def LogoutView(request):
    logout(request)
    return redirect("/login")


def UploadView(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login_error.html')
    current_user = request.user
    if request.method == "POST":
        song_info = mutagen.File(request.FILES["mysong"])
        song = Song.objects.create(
            title="".join(song_info["TIT2"].text),
            artist="".join(song_info["TPE1"].text),
            album="".join(song_info["TALB"].text),
            path=request.FILES["mysong"],
            tracknumber="".join(song_info["TRCK"].text)
        )
        song.user.add(current_user)
        song.save()
        redirect("upload")

    return render(request, "song_upload.html")


def PlayView(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login_error.html')
    current_user = request.user
    my_songs = current_user.user_songs.all()
    songs = Song.objects.all()

    if request.POST.get("play"):
        song_id = request.POST.get("play")
        song = Song.objects.get(id=song_id)
        global player
        player = vlc.MediaPlayer(song.path.path)
        player.play()
    if request.POST.get("stop"):
        player.stop()
    if request.POST.get("pause"):
        player.pause()

    if request.POST.get("delete"):
        song_id = request.POST.get("delete")
        song = Song.objects.get(id=song_id)
        song.delete()

    return render(request, "play.html", {
        "songs": songs,
        "my_songs": my_songs
        }
    )
