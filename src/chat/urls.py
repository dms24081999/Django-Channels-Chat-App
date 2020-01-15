from django.urls import path, re_path


from .views import ThreadView, InboxView

app_name = 'chat'
urlpatterns = [
    path("", InboxView.as_view()),
    path("<username>", ThreadView.as_view()),
]