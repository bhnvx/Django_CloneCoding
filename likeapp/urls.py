from django.urls import path

from likeapp.views import LikeArticleView
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'likeapp'

urlpatterns = [
    path('article/like/<int:pk>', LikeArticleView.as_view(), name='article_like'),
]
