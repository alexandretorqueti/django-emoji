from django.urls import re_path as url

from .views import EmojiJSONListView

app_name = "emoji"
urlpatterns = [
    url(r'^all.json$', EmojiJSONListView.as_view(), name='list.json'),
]
