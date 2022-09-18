from django.shortcuts import render
from .models import News, Job, InternationalNews
from .serializers import NewsSerializer, JobSerializer, InternationalNewsSerializer
from datetime import datetime
from rest_framework import generics
from django.http import HttpResponse
from .jobs import add_job
from .adding_news import add_international_news, add_news

today = datetime.now()


class NewsList(generics.ListAPIView):
    # queryset = News.objects.filter(date_posted__contains=today.strftime("%b")).order_by('-id')
    # queryset = News.objects.order_by('-id')
    queryset = News.objects.filter(date_posted=today.strftime("%B %d, %Y"))
    serializer_class = NewsSerializer

    # search_fields = ('^')


class JobList(generics.ListAPIView):
    queryset = Job.objects.order_by('-id')
    serializer_class = JobSerializer


class InternationalNewsList(generics.ListAPIView):
    queryset = InternationalNews.objects.order_by('-id')
    serializer_class = InternationalNewsSerializer


def update(request):
    add_job()
    add_international_news()
    add_news()

    return HttpResponse("Updated!")