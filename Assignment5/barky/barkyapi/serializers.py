from .models import Bookmark

from rest_framework import serializers


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ("id", "title", "url", "notes", "date_added")

