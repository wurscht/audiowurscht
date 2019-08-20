from django.contrib.auth import views as auth_views
from django.urls import path
from webapp import views
from django.conf import settings
from django.conf.urls.static import static
from webapp.forms import LoginForm


urlpatterns = [
    path("", views.MenuView, name="menu"),
    path(
        "register/",
        views.RegistrationView.as_view(),
        name="register"
    ),
    path(
        "registration_done/<str:key>/",
        views.RegistrationDoneView.as_view(),
        name="registrationdone"
    ),
    path(
        "send_confirmation_mail/",
        views.send_confirmation_mail_view,
        name="sendconfirmation"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(),
        {'authentication_form': LoginForm},
        name="login"
    ),
    path(
        "logout/",
        views.LogoutView,
        name="logout"
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="passwordchange"
    ),
    path(
        "password_change_done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done"
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),
    path(
        "password_reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    path(
        "password_reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="passwordresetconfirm"
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="passwordresetcomplete"
    ),
    path("upload/", views.UploadView, name="upload"),
    path("play/", views.PlayView, name="play"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
