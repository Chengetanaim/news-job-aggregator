from rest_framework import serializers
from .models import News, Job, InternationalNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'link', 'image', 'date_posted')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title', 'link')


class InternationalNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalNews
        fields = ('id', 'title', 'link', 'description', 'image')



