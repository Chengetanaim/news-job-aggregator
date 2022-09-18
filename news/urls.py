from django.urls import path
from .views import NewsList, JobList, InternationalNewsList
from . import views


urlpatterns = [
    path('news/', NewsList.as_view()),
    path('jobs/', JobList.as_view()),
    path('international-news/', InternationalNewsList.as_view()),
    path('update/', views.update),
]
