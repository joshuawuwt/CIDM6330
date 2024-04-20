from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Bookmark
from .permissions import IsOwnerOrReadOnly
from .serializers import BookmarkSerializer


# Create your views here.
class BookmarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookmarks to be viewed or edited.
    """

    queryset = Bookmark.objects.all().order_by("-date_added")
    serializer_class = BookmarkSerializer


